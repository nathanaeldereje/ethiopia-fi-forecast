# Data Enrichment Log
**Project:** Ethiopia Financial Inclusion Forecasting
**Task:** 1 - Data Exploration & Enrichment
**Date:** 28 Jan 2026
**Author:** [Your Name]

## 1. Overview of Changes
The starter dataset contained sparse Findex survey data (2011, 2014, 2017, 2021, 2024). To enable accurate forecasting for 2025-2027, I enriched the dataset with high-frequency administrative data and infrastructure proxies.

## 2. Added Observations (Data Points)

| Pillar | Indicator | Year/Date | Value | Source | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Infrastructure** | Mobile Penetration | Jan 2023 | **53.5%** | DataReportal Digital 2023 | Functions as a "ceiling" for digital adoption; strong proxy for potential access. |
| **Infrastructure** | Mobile Penetration | Jan 2024 | **60.4%** | DataReportal Digital 2024 | Tracks the rapid expansion of 4G/network availability. |
| **Usage** | Telebirr Registered Users | Jan 2023 | **27.2 M** | EthioTelecom H1 Report | Fills the usage gap between Findex 2021 and 2024. |
| **Usage** | Telebirr Registered Users | June 2024 | **47.55 M** | EthioTelecom Annual Report | Shows the acceleration of adoption (leading indicator for Findex Usage). |

## 3. Added Events (Context)

| Category | Event Name | Date | Source | Impact Hypothesis |
| :--- | :--- | :--- | :--- | :--- |
| **Product Launch** | Safaricom M-Pesa Launch | **16 Aug 2023** | Safaricom Press Release | Introduces competition; expected to increase Usage rates due to market marketing spend. |
| **Policy** | NBE Mobile Money Directive | **Oct 2023** | National Bank of Ethiopia | Increased transaction limits likely drove higher volume/value usage in late 2023. |

## 4. Data Quality Notes
*   **Confidence:** High. All added data comes from primary source reports (EthioTelecom) or widely cited aggregators (DataReportal/ITU).
*   **Transformation:** Telebirr user counts were converted from raw text ("27.2 Million") to numeric integers for analysis.
*   **Alignment:** Mapped "Mobile Penetration" to `ACC_MOBILE_PEN` to maintain schema consistency.