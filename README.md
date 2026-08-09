# Fed Language and Financial Markets

## Research Question

Does the tone of FOMC statements predict movements in Treasury yields and market volatility?

## Overview

This empirical research project examines whether the language used in Federal Open Market Committee (FOMC) statements contains information about financial market reactions around monetary policy announcements.

The analysis combines natural language processing with event study methods and regression analysis to study the relationship between unexpected FOMC communication and movements in Treasury yields and market volatility.

## Data

The sample contains 40 FOMC statements from January 2021 through December 2024.

Market data are obtained from the Federal Reserve Bank of St. Louis FRED database and include:

* 2 Year Treasury yield
* 10 Year Treasury yield
* VIX index
* Federal Funds Rate

For each FOMC announcement, market reactions are measured using both one trading day and two trading day event windows.

## Methodology

### 1. FOMC Statement Processing

FOMC statements are cleaned and processed to remove non statement content.

### 2. Communication Measure

A dictionary based measure is used to classify hawkish and dovish language.

The hawkishness score is calculated as the difference between hawkish and dovish word counts, normalized by the total number of words and scaled by 1,000.

### 3. Unexpected Communication

Hawkishness is regressed on the contemporaneous change in the Federal Funds Rate.

The residual from this regression is used as the unexpected communication measure.

This separates the communication component from the contemporaneous policy rate movement.

### 4. Event Study

Market reactions are measured as changes between the last trading day before an FOMC announcement and the first trading day after the announcement.

Both one day and two day event windows are examined.

### 5. Regression Analysis

The main specification estimates the relationship between unexpected FOMC communication and market reactions:

$$
Reaction_i =
\alpha +
\beta UnexpectedTone_i +
\epsilon_i
$$

Heteroskedasticity robust HC1 standard errors are used.

### 6. Influence Analysis

Cook's distance is used to identify observations with relatively high influence on the regression estimates.

Robustness specifications exclude the three observations with the highest Cook's distance.

## Main Findings

The main one day event window results show a negative and statistically significant association between unexpected FOMC communication and Treasury yields.

| Outcome | Coefficient | P value | R squared | N |
|---|---:|---:|---:|---:|
| 2Y Treasury | −0.00784 | 0.030 | 0.128 | 39 |
| 10Y Treasury | −0.00679 | 0.016 | 0.141 | 39 |
| VIX | 0.03155 | 0.544 | 0.008 | 39 |

The results indicate that unexpected FOMC communication is associated with Treasury yield movements, while no statistically significant relationship is detected for the VIX.

The two day event window produces similar negative coefficients for both Treasury yields. The 2 Year coefficient is −0.00684 with a p value of 0.057, while the 10 Year coefficient is −0.00636 with a p value of 0.043.

## Robustness

The influence analysis supports the main one day Treasury results.

After excluding the three observations with the highest Cook's distance:

| Outcome | Coefficient | P value | R squared | N |
|---|---:|---:|---:|---:|
| 2Y Treasury | −0.00563 | 0.029 | 0.082 | 36 |
| 10Y Treasury | −0.00568 | 0.044 | 0.099 | 36 |

For the two day window, the 2 Year result remains statistically significant after excluding influential observations, while the 10 Year result becomes statistically insignificant.

These results suggest that the main announcement day findings are not driven entirely by a small number of influential observations.

## Interpretation

The findings are consistent with FOMC statement language containing information associated with Treasury market movements beyond the contemporaneous Federal Funds Rate change.

The strongest evidence is concentrated in the announcement day response and in the 2 Year Treasury yield.

The analysis identifies statistical associations rather than causal effects. The relatively small sample and dictionary based communication measure also motivate cautious interpretation.

## Repository Structure

```text
prediction-markets-fed-policy-forecasting/
│
├── data/
│   ├── DFF.csv
│   ├── fomc_dates.csv
│   ├── fomc_dff_decisions.csv
│   ├── fomc_statements_clean.csv
│   ├── market_data_clean.csv
│   └── regression_results.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_market_data.ipynb
│
├── src/
│   └── text_features.py
│
├── figures/
│   ├── fomc_tone_2y_reaction.png
│   ├── fomc_tone_10y_reaction.png
│   ├── fomc_tone_vix_reaction.png
│   └── hawkishness_distribution.png
│
├── paper/
│   ├── methodology.md
│   └── results.md
│
└── README.md