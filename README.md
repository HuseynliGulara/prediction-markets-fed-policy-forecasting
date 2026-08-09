# Fed Language and Financial Markets

## Research Question

Does FOMC statement language contain information about Treasury market movements beyond the contemporaneous Federal Funds Rate change?

## Objective

This project studies whether the language of Federal Open Market Committee (FOMC) statements is associated with Treasury yield movements around monetary policy announcements.

The analysis focuses on whether FOMC communication contains information beyond the mechanical effect of the policy rate decision.

## Data

The project uses:

* FOMC statements from January 2021 through December 2024
* 2 Year Treasury Yield
* 10 Year Treasury Yield
* VIX
* Federal Funds Rate

Market data are obtained from the Federal Reserve Economic Data (FRED) database.

The final sample contains 40 FOMC announcements.

## Methodology

The analysis consists of four main steps:

1. Extract and clean FOMC statement text.
2. Construct a normalized hawkishness measure using hawkish and dovish language.
3. Construct an unexpected communication measure by removing the component of hawkishness associated with the Federal Funds Rate change.
4. Estimate event study regressions using Treasury yield and VIX changes around FOMC announcements.

The main event window measures the change from the last trading day before the FOMC announcement to the first trading day after the announcement.

Heteroskedasticity robust standard errors are used in the regression analysis.

## Preliminary Results

The preliminary results show a statistically significant association between unexpected FOMC communication and Treasury yield movements.

| Outcome | Coefficient | P value | R squared |
|---|---:|---:|---:|
| 2 Year Treasury | −0.00784 | 0.030 | 0.128 |
| 10 Year Treasury | −0.00679 | 0.016 | 0.141 |
| VIX | 0.03155 | 0.544 | 0.008 |

The association is statistically significant for both the 2 Year and 10 Year Treasury yields, while no statistically significant relationship is found for the VIX.

These results are preliminary and should not be interpreted as causal evidence.

## Robustness

A two trading day event window is also examined.

The association remains statistically significant for the 10 Year Treasury yield, while the 2 Year Treasury result becomes significant at the 10 percent level.

Further robustness analysis will examine alternative communication measures and event windows.

## Repository Structure

```text
data/
    Raw and processed datasets

notebooks/
    Jupyter notebooks containing the empirical analysis

src/
    Reusable Python functions

figures/
    Research figures

paper/
    Research documentation and results
