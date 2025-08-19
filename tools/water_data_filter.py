# tools/water_data_filter.py
"""
Water Data Intelligence Layer v0.1
Filters Arizona water datasets based on anomaly detection needs
"""

import requests
import pandas as pd
from datetime import datetime
import yaml
import os

# Supported portals
PORTALS = {
    'phoenix': 'https://data.phoenix.gov',
    'tucson': 'https://data.tucsonaz.gov',
    'maricopa': 'https://data.maricopa.gov'
}

# Evaluation weights (your expert judgment)
CRITERIA_WEIGHTS = {
    'has_zip_code': 3,
    'residential_only': 3,
    'monthly_updates': 2,
    'recent_data': 2,
    'direct_api': 2
}

def search_water_datasets():
    """Find water-related datasets"""
    results = []
    for city, base_url in PORTALS.items():
        try:
            response = requests.get(
                f"{base_url}/api/catalog/v1",
                params={'q': 'water', 'limit': 10}
            )
            data = response.json()
            
            for item in data.get('results', []):
                resource = item.get('resource', {})
                metadata = {
                    'city': city,
                    'title': resource.get('name', 'No title'),
                    'description': resource.get('description', '')[:300],
                    'url': item.get('permalink', ''),
                    'api_endpoint': resource.get('apiEndpoint', ''),
                    'updated_at': resource.get('updatedAt', ''),
                    'row_count': resource.get('rowCount', 0),
                    'tags': [t.lower() for t in resource.get('tags', [])]
                }
                results.append(metadata)
        except Exception as e:
            print(f"Error fetching {city}: {e}")
    return pd.DataFrame(results)

def evaluate_dataset(row):
    """Apply your expert criteria"""
    score = 0
    feedback = []
    
    # 1. Zip code granularity
    has_zip = any(kw in (row['title'] + ' ' + row['description']).lower() 
                  for kw in ['zip', 'zipcode', 'postal', 'neighborhood'])
    if has_zip:
        score += CRITERIA_WEIGHTS['has_zip_code']
        feedback.append("✅ Zip code data")
    else:
        feedback.append("❌ No zip code mention")
    
    # 2. Residential focus
    has_res = any(kw in (row['tags']) for kw in ['residential', 'household']) or \
              'residential' in (row['title'] + row['description']).lower()
    if has_res:
        score += CRITERIA_WEIGHTS['residential_only']
        feedback.append("✅ Residential focus")
    else:
        feedback.append("❌ No residential tag")
    
    # 3. Update frequency (proxy: recent update)
    try:
        updated = pd.to_datetime(row['updated_at'])
        months_old = (pd.Timestamp.now() - updated).days / 30
        if months_old < 6:
            score += CRITERIA_WEIGHTS['monthly_updates']
            feedback.append("✅ Recently updated")
        else:
            feedback.append(f"❌ Last updated {months_old:.1f}mo ago")
    except:
        feedback.append("❌ Unknown update date")
    
    # 4. Recent data range
    has_recent = any(kw in (row['description'] + row['title']).lower() 
                     for kw in ['2020', '2021', '2022', '2023', '2024'])
    if has_recent:
        score += CRITERIA_WEIGHTS['recent_data']
        feedback.append("✅ Recent years")
    
    # 5. Direct API
    if pd.notna(row['api_endpoint']) and 'socrata' in row['api_endpoint']:
        score += CRITERIA_WEIGHTS['direct_api']
        feedback.append("✅ API available")
    else:
        feedback.append("❌ No direct API")
    
    return score, " | ".join(feedback)

def generate_config():
    """Run the intelligence layer"""
    print("🔍 Searching Arizona water datasets...")
    df = search_water_datasets()
    
    print(f"Found {len(df)} datasets. Evaluating...")
    df[['score', 'feedback']] = df.apply(
        lambda x: pd.Series(evaluate_dataset(x)), axis=1
    )
    
    # Sort by score
    df = df.sort_values('score', ascending=False)
    
    # Save results
    df.to_csv('results_water_evaluation.csv', index=False)
    print("Saved full evaluation to CSV")
    
    # Create config for best dataset
    if len(df) > 0:
        best = df.iloc[0]
        config = {
            'primary_dataset': {
                'source': f"{best['city']}: {best['title']}",
                'url': best['url'],
                'api_endpoint': best['api_endpoint'],
                'selection_reason': best['feedback'],
                'confidence_score': int(best['score']),
                'selected_at': datetime.now().isoformat()
            },
            'criteria_weights': CRITERIA_WEIGHTS,
            'evaluation_timestamp': datetime.now().isoformat()
        }
        
        # Save config
        os.makedirs('config', exist_ok=True)
        with open('config/data_config.yaml', 'w') as f:
            yaml.dump(config, f, indent=2)
            
        print(f"\n🏆 Top Dataset: {best['title']} ({best['city']})")
        print(f"Score: {best['score']}/12")
        print(f"Feedback: {best['feedback']}")
        print("Config saved to config/data_config.yaml")
        
        return config
    
    return None

if __name__ == "__main__":
    config = generate_config()
