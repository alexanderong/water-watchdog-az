# Water Dataset Evaluation Criteria

For anomaly detection in residential water use, I prioritize:

1. **Granularity**  
   ✅ Must have zip code or neighborhood-level data  
   ❌ City-wide averages are useless for targeting

2. **Residential Segmentation**  
   ✅ Must separate residential from commercial/industrial  
   ❌ Mixed-use data hides household waste

3. **Update Frequency**  
   ✅ Monthly or more frequent  
   ❌ Annual data is too slow for anomaly alerts

4. **Time Range**  
   ✅ 2020–present (covers post-pandemic norms)  
   ❌ Older data may not reflect current usage

5. **Public Accessibility**  
   ✅ Direct CSV/JSON API  
   ❌ PDF reports or login walls are not usable

6. **Field Clarity**  
   ✅ Clear column names (e.g., `gallons_per_capita`)  
   ❌ Ambiguous fields like `usage_value` are risky
