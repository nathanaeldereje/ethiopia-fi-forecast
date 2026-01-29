# 📈 Forecasting Financial Inclusion in Ethiopia
**Project:** 10 Academy: Artificial Intelligence Mastery - Week 10 Challenge  
**Role:** Data Scientist (Selam Analytics)  
**Status:** 🚧 In Progress

## Project Overview
This project empowers **Selam Analytics** and its consortium of stakeholders (National Bank of Ethiopia, Mobile Operators, DFIs) to track and predict the trajectory of digital financial transformation in Ethiopia. By integrating historical survey data with event-based modeling, we aim to forecast financial inclusion outcomes.

Using a unified data schema, the system analyzes the impact of key events (e.g., the launch of Telebirr, M-Pesa, and new NBE policies) to predict future trends in account ownership and digital payment usage.
**Goal:** Provide actionable insights into what drives financial inclusion and forecast Access and Usage metrics for **2025–2027**.

## 📖 Business Objective
**Selam Analytics** is a fintech consulting firm addressing a critical paradox in the Ethiopian market: While digital infrastructure and mobile money users (Telebirr: 54M+) are exploding, the percentage of adults with a financial account has stagnated (49% in 2024, only +3pp since 2021).

*   **The Problem:** Traditional analysis fails to explain the gap between massive infrastructure growth and slow adoption of registered financial accounts. Stakeholders need to know *why* inclusion is lagging and *where* it is heading.
*   **The Solution:** A forecasting system that quantifies the impact of product launches and policy changes on inclusion metrics, moving beyond simple trendlines to event-aware predictive modeling.

**Key Performance Indicators (KPIs):**
*   **Access (Account Ownership):** % of adults (15+) with an account at a bank or mobile money provider.
*   **Usage (Digital Payments):** % of adults who made or received a digital payment in the past 12 months.
*   **Event Impact:** Quantifiable magnitude of specific events (e.g., "Telebirr Launch") on national inclusion rates.

## 📊 Data & Assets
The analysis utilizes a **Unified Schema** combining World Bank Global Findex surveys, NBE reports, and operator data.

| Data Type | Description | Key Indicators | Source |
| :--- | :--- | :--- | :--- |
| **Observations** | Measured values from surveys/reports | Account Ownership, Digital Payments, Gender Gap | Findex, NBE, GSMA |
| **Events** | Qualitative milestones | Product Launches (Telebirr, M-Pesa), Policies (NBE Directives) | News, Official Gazettes |
| **Impact Links** | Modeled relationships | Effect Magnitude, Lag Periods, Direction | Derived/Modeled |
| **Targets** | Official Policy Goals | NFIS Strategy Targets | Government Documents |

## 📂 Repository Structure
```text
ethiopia-fi-forecast/
├── .github/workflows/  # CI/CD for automated testing
├── data/               
│   ├── raw/            # Starter dataset (ethiopia_fi_unified_data.csv)
│   └── processed/      # Analysis-ready enriched data
├── notebooks/          # Jupyter Notebooks for EDA, Modeling, and Forecasting
├── src/                # Source code for data loader and logic
├── dashboard/          # Streamlit application
├── tests/              # Unit tests
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🛠️ Getting Started

### Prerequisites
*   Python 3.10+
*   Streamlit
*   VS Code or Jupyter Lab

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/nathanaeldereje/ethiopia-fi-forecast.git
    cd ethiopia-fi-forecast
    ```

2.  **Set up the environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Tests**
    Ensure the environment is set up correctly by running the initial tests:
    ```bash
    pytest
    ```

## 🔄 Recommended Workflow

1.  **Data Exploration & Enrichment (Task 1)**
    *   Load the unified dataset, understand the schema (observation vs. event), and enrich with external data (e.g., GSMA infrastructure data, gender-disaggregated stats).
    *   **Run:** `notebooks/01_data_enrichment.ipynb`
    *   *Key Output:* `data/processed/enriched_data.csv` and data enrichment logs.

2.  **Exploratory Data Analysis (Task 2)**
    *   Analyze the "Access vs. Usage" gap, gender disparities, and timeline of major market events (Telebirr/M-Pesa).
    *   **Run:** `notebooks/02_eda.ipynb`
    *   *Key Output:* Visualization of Ethiopia's financial inclusion trajectory vs. infrastructure growth.

3.  **Event Impact Modeling (Task 3)**
    *   Construct an "Association Matrix" to quantify how specific events (Policies, Product Launches) impact inclusion indicators.
    *   **Run:** `notebooks/03_impact_modeling.ipynb`
    *   *Key Output:* Event-Indicator Association Matrix (Heatmap) and estimated lag effects.

4.  **Forecasting Access and Usage (Task 4)**
    *   Generate forecasts for 2025-2027 using event-augmented trend models and scenario analysis (Optimistic vs. Pessimistic).
    *   **Run:** `notebooks/04_forecasting.ipynb`
    *   *Key Output:* Forecast tables with confidence intervals for Account Ownership and Digital Payments.

5.  **Dashboard Development (Task 5)**
    *   Build an interactive Streamlit dashboard to present findings and allow stakeholders to simulate scenarios.
    *   **Run:** `streamlit run dashboard/app.py`
    *   *Key Output:* Interactive web app displaying P2P trends, forecasts, and scenario selectors.

## 🚀 Project Progress & Roadmap (as of January 28, 2026)

| Phase | Task Description | Status |
| :--- | :--- | :--- |
| **0. Setup** | Project Structure, Git, CI/CD, and Environment Setup | ✅ Completed |
| **1. Enrich** | Data Enrichment (Task 1) - Adding external indicators | ✅ Completed |
| **2. Explore** | EDA (Task 2) - Visualizing the "Access-Usage" Gap | ⏳ Pending |
| **3. Model** | Impact Modeling (Task 3) - Quantifying event effects | 🚧 In Progress |
| **4. Forecast** | Projections (Task 4) - Predicting 2025-2027 outcomes | ⏳ Pending |
| **5. Visualize** | Dashboard (Task 5) - Streamlit App Development | ⏳ Pending |

## 📸 Visuals
*(Placeholders for future outputs)*

*   **Timeline:** *[Insert Plot of Events overlaying Account Ownership]*
*   **Forecast:** *[Insert Fan Chart of 2025-2027 Projections]*
*   **Dashboard:** *[Insert Screenshot of Streamlit App]*

---
*Date: January, 2026*