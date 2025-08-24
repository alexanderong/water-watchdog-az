# Arizona Drought Risk Framework  
**A Data-Driven Approach to County-Level Drought Analysis**

> *Version 1.0*  
> *Author: Alexander Ong*  
> *Date: 2025-08-20*

---

## 1. 🎯 Research Question

### Primary Question
> "How do drought impacts vary across Arizona counties — and what socioeconomic and geographic factors explain differences in resilience?"

### Sub-Questions
1. Do counties with higher socioeconomic vulnerability experience longer recovery times after extreme drought?
2. Are drought conditions spatially correlated between neighboring counties?
3. Can we predict future drought risk using historical patterns and structural factors?

---

## 2. 🧩 Conceptual Framework

This framework is based on the **IPCC Risk Model** (AR6):  
> **Risk = Hazard × Exposure × Vulnerability**

This model is widely used in climate risk assessment (IPCC, CDC, USDA) and provides a defensible, peer-reviewed foundation for analyzing drought risk.

| Component | Definition | Data Source |
|---------|-----------|-----------|
| **Hazard** | Drought severity and duration | U.S. Drought Monitor (USDM) |
| **Exposure** | Population and economic assets in affected areas | U.S. Census |
| **Vulnerability** | Socioeconomic capacity to cope with drought | U.S. Census, BIA, ADWR |
| *(Optional) Adaptive Capacity* | Infrastructure, policy, and resources to respond | ADWR, city reports |

This framework ensures the analysis is not just descriptive, but **causal and policy-relevant**.

---

## 3. 🗃️ Data Inventory

| Dataset | Source | Use Case | Access Status |
|--------|--------|--------|----------------|
| **U.S. Drought Monitor (USDM)** | [drought.gov](https://drought.gov) | Hazard (D0–D4 by county) | ✅ Public, weekly (2000–2022) |
| **U.S. Census ACS 5-Year Estimates** | [data.census.gov](https://data.census.gov) | Population, income, education, housing | ✅ Public |
| **ADWR Active Management Areas (AMAs)** | [azwater.gov](https://azwater.gov) | Adaptive capacity (groundwater regulation) | ✅ Public |
| **Tribal Land Boundaries** | [BIA GIS](https://www.bia.gov/service/gis) | Vulnerability (water access disparities) | ✅ Public |
| **Arizona River Basins** | [ADWR Hydrology](https://azwater.gov/hydrology) | Physical connectivity | ✅ Public |
| **Crop Water Use (SWAP Model)** | [UA SWAT Lab](https://cals.arizona.edu/swat/) | Economic dependence on water | ✅ Public |

All datasets are **publicly available**, **citatable**, and **defensible** for academic or policy use.

---

## 4. 🧮 Analytical Plan

### Phase 1: Hazard Characterization
- Compute **Weighted Drought Severity Index (wDSI)**  
  `wDSI = D1×1 + D2×2 + D3×4 + D4×8`  
  *(Exponential weights reflect increasing severity)*
- Identify **drought events** (wDSI > 300)
- Measure **duration** and **recovery time** (weeks to return to D1 or lower)

### Phase 2: Exposure & Vulnerability Scoring
- Pull **Census data** for all AZ counties (2020 ACS 5-year)
- Build **Socioeconomic Vulnerability Index (SVI)** using:
  - % below poverty line
  - % without vehicle access
  - % elderly (65+)
  - % no high school diploma
  - % linguistic isolation
- Normalize and combine into a 0–1 index

### Phase 3: Test Hypothesis
> **"Counties with higher socioeconomic vulnerability take longer to recover from drought."**

- Merge SVI with drought recovery time
- Compute **Pearson correlation**
- Visualize with **scatterplot + trendline**
- Report **r, p-value, and effect size**

### Phase 4: Spatial & Systemic Analysis (Optional)
- Map **shared river basins** and aquifers
- Compute **spatial autocorrelation** (e.g., Moran’s I)
- Identify **high-risk clusters** (e.g., Navajo + Apache + Coconino)

---

## 5. 📚 Academic & Policy Anchors

| Source | Relevance |
|-------|----------|
| [Cutter et al., 2003 – Social Vulnerability Index](https://doi.org/10.1175/1520-0477(2003)84<2493:SVITOT>2.3.CO;2) | Validates SVI approach |
| [IPCC AR6 Chapter 12](https://www.ipcc.ch/report/ar6/wg2/) | Risk = Hazard × Exposure × Vulnerability |
| [ADWR 2023 Drought Preparedness Plan](https://azwater.gov/drought) | Local policy context |
| [CDC Social Vulnerability Index (SVI)](https://svi.cdc.gov) | Public health parallel |

This project applies **peer-reviewed frameworks** to local data — not inventing, but **replicating and validating** at the county level.

---

## 6. ⚠️ Assumptions & Limitations

| Item | Assumption | Limitation |
|------|------------|-----------|
| wDSI weights | D4 is 8× more severe than D1 | Simplifies complex reality |
| Recovery time | Return to D1 = recovery | Ignores groundwater lag |
| SVI | Linear combination of factors | Doesn’t capture tribal sovereignty |
| Data | USDM is accurate and consistent | Some counties have gaps |
| Correlation | Linear relationship | May miss non-linear dynamics |

> Transparency about limitations **increases credibility**, not reduces it.

---

This framework is **not static** — it will evolve as data and insights develop.
