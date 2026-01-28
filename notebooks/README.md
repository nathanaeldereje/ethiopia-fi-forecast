# 📓 Financial Inclusion Forecasting Notebooks

This directory contains the Jupyter Notebooks used for the step-by-step data enrichment, exploratory analysis, impact modeling, and forecasting for the Ethiopia Financial Inclusion project.

## 📂 Notebook Directory

| Order | Notebook Name | Description | Key Tasks & Outputs |
| :--- | :--- | :--- | :--- |
| **01** | `01_data_enrichment.ipynb` | **Task 1: Data Exploration & Enrichment**<br>Loads the unified schema, understands event structures, and merges external datasets. | • Load `ethiopia_fi_unified_data.csv`<br>• Map `record_type` (observation vs event)<br>• Add external indicators (GSMA, NBE)<br>• Document Data Sources |
| **02** | `02_eda.ipynb` | **Task 2: Exploratory Data Analysis**<br>Analyzes historical trends, the "Access vs. Usage" gap, and visualizes the event timeline. | • Access (Account) vs Usage (Payments) Trends<br>• Gender Gap & Infrastructure Analysis<br>• Event Timeline Visualization (Telebirr, M-Pesa)<br>• Correlation Heatmaps |
| **03** | `03_impact_modeling.ipynb` | **Task 3: Event Impact Modeling**<br>Quantifies how specific events (policies, product launches) shift inclusion curves. | • Event-Indicator Association Matrix<br>• Estimate Impact Magnitude & Lags<br>• Proxy Analysis (comparable country data)<br>• Quantify "Telebirr Effect" |
| **04** | `04_forecasting.ipynb` | **Task 4: Forecasting 2025-2027**<br>Generates future projections for Access and Usage using event-augmented trends. | • Baseline Trend Regression<br>• Scenario Analysis (Optimistic/Base/Pessimistic)<br>• Confidence Intervals (Fan Charts)<br>• 2027 Target Projections |

## 🛠️ Setup & Usage

To ensure you can import functions from the `src/` module (e.g., your data loaders or model logic), each notebook includes a path injection block at the top.

**Standard Import Block**
At the top of each notebook, you should run:

```python
import sys
import os

# Add the parent directory to sys.path to access src/
sys.path.append(os.path.abspath(os.path.join('..')))

# Example import from custom modules
from src.loader import load_data
from src.utils import plot_timeline
```