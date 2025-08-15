# AIFB_8030
# 🧠 Intelligent Demand Forecasting & Reorder System

> A Decision Support System (DSS) for retail demand forecasting and inventory reorder planning.  
> Combines **classical ML** (e.g., RandomForest) and **Generative‑AI–adjacent time series** via **Prophet**, with an interactive **Streamlit** dashboard for non‑technical users.

---

## 🔗 Quick Links
- **Demo (local):** `streamlit run app.py`
- **Report:** `AIML FINAL REPORT.docx`
- **Slides:** `AIML_FINAL_REPORT_PRESENTATION.pptx`
- **Dataset:** FreshRetailNet‑50K (see below)

---

## 📚 Table of Contents
1. [Project Overview](#project-overview)
2. [Business Problem](#business-problem)
3. [Data](#data)
4. [Techniques](#techniques)
5. [Repository Structure](#repository-structure)
6. [Setup & Run](#setup--run)
7. [Dashboard (Streamlit)](#dashboard-streamlit)
8. [Results & Benchmarks](#results--benchmarks)
9. [Prototype Design](#prototype-design)
10. [Integration Plan](#integration-plan)
11. [Change Management Plan](#change-management-plan)
12. [Performance Management Plan](#performance-management-plan)
13. [Ethics, Equity, Privacy, Security, Sustainability, Well-being](#ethics-equity-privacy-security-sustainability-well-being)
14. [Key Trade‑offs & Design Decisions](#key-trade-offs--design-decisions)
15. [Roadmap](#roadmap)
16. [Citations](#citations)
17. [License](#license)

---

## Project Overview
Retailers struggle with **stockouts** and **overstocking**. This DSS predicts demand and recommends reorder points, integrating smoothly with existing **Excel/ERP** workflows.

**What it does**
- Forecasts demand per **SKU × store**.
- Recommends **reorder dates/quantities**.
- Lets users compare **Classical ML vs Prophet**.
- Presents results in a friendly **Streamlit** dashboard.

**Who it’s for**
- Retail Managers • Inventory Planners • Business Analysts • IT Admins • Sponsors

---

## Business Problem
- Minimize **lost sales** from stockouts and **waste** from overstock.
- Replace manual Excel heuristics with **auditable, transparent** forecasts and reorder logic.

---

## Data
**FreshRetailNet‑50K**  
- ~50,000 hourly time series across 898 stores & 863 perishable SKUs (sales, inventory, stockout flags, promos, weather).  
- Includes **latent demand during stockouts** → ideal for reorder training.

**Sources**
- GitHub: `https://github.com/hoshigan/Supply-Chain-Analytic---Just-In-Time-Company`
- Paper: `https://arxiv.org/abs/2505.16319`

**Important columns**: `ds` (date), `y` (target demand), `inventory`, `stockout_flag`, `promotion_flag`, `store_id`, `sku`.

---

## Techniques
- **Without GenAI (Classical ML):** Linear Regression, Random Forest; feature engineering (dayofweek, month, lags), evaluation (MAE/RMSE/R²).
- **With GenAI‑style Time Series:** **Prophet** (trend/seasonality/holidays), optional regressors (promotion_flag, day_of_week), uncertainty intervals.
- **Optimization logic (simple):** reorder point suggestion using demand × lead‑time ± safety buffer.
- **Visualization:** Streamlit + Matplotlib/Plotly.

---

## Repository Structure
- ├─ app.py # Streamlit dashboard
├─ notebooks/
│ ├─ A2.ipynb # EDA, modeling, comparisons
├─ data/
│ ├─ engineered_dataset.csv # feature‑engineered dataset
│ ├─ prophet_forecast.csv # Prophet outputs
│ └─ reorder_plan_all_products.csv
├─ assets/
│ ├─ architecture.png # (TODO: add)
│ ├─ integration_diagram.png # (TODO: add)
│ ├─ wireframe_low.png # (TODO: add)
│ └─ wireframe_high.png # (TODO: add)
├─ requirements.txt
└─ README.md
