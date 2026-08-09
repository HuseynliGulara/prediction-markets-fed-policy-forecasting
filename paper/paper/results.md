# Empirical Results

## Research Question

This study examines whether the tone of Federal Open Market Committee (FOMC) statements is associated with movements in Treasury yields around monetary policy announcements.

## Data

The sample contains 40 FOMC statements from January 2021 through December 2024. Market data include 2 Year Treasury yields, 10 Year Treasury yields, the VIX index, and the Federal Funds Rate from FRED.

For each FOMC announcement, the market reaction is measured as the change between the last trading day before the announcement and the first trading day after the announcement.

A two trading day event window is also examined as a robustness check.

## Communication Measure

FOMC statement language is classified using a dictionary based measure of hawkish and dovish terms. The resulting hawkishness measure is normalized by statement length.

To separate communication content from the contemporaneous policy rate movement, hawkishness is regressed on the change in the Federal Funds Rate. The residual from this regression is used as the unexpected communication component.

This approach separates the component of FOMC communication that is not explained by the contemporaneous policy rate change.

## Main Results

The regression results show a statistically significant negative association between unexpected FOMC communication and Treasury yield movements during the announcement window.

For the 2 Year Treasury yield, the coefficient on unexpected tone is −0.00784 with a p value of 0.030. The model has an R squared of 0.128.

For the 10 Year Treasury yield, the coefficient is −0.00679 with a p value of 0.016. The model has an R squared of 0.141.

For the VIX, the coefficient is 0.03155 with a p value of 0.544, indicating no statistically significant association between unexpected FOMC communication and the change in market volatility.

The Treasury results suggest that unexpected variation in FOMC communication is associated with movements in both short and longer maturity Treasury yields, while the evidence for market volatility is weak.

## Two Day Event Window

The two trading day event window produces similar coefficient estimates.

For the 2 Year Treasury yield, the coefficient is −0.00684 with a p value of 0.057 and an R squared of 0.081.

For the 10 Year Treasury yield, the coefficient is −0.00636 with a p value of 0.043 and an R squared of 0.093.

These results suggest that the negative association remains present over a slightly longer event window, although the statistical evidence is weaker for the 2 Year Treasury yield.

## Influence Robustness

An influence analysis based on Cook's distance is used to identify observations that have relatively high influence on the regression estimates.

For the one day 2 Year Treasury specification, the three observations with the highest Cook's distance are March 16, 2022, March 22, 2023, and December 13, 2023.

These observations are retained in the main specification because they represent genuine monetary policy events rather than data errors.

As a robustness check, these three observations are excluded and the regression is re estimated using heteroskedasticity robust HC1 standard errors.

For the 2 Year Treasury yield, the coefficient remains negative at −0.00563 with a p value of 0.029 and an R squared of 0.082.

For the 10 Year Treasury yield, the coefficient remains negative at −0.00568 with a p value of 0.044 and an R squared of 0.099.

The persistence of the negative coefficient and statistical significance suggests that the main one day Treasury results are not driven entirely by the most influential observations.

## Two Day Influence Robustness

The influence robustness analysis is also applied to the two day event window.

For the 2 Year Treasury yield, the three observations with the highest Cook's distance are March 16, 2022, March 22, 2023, and July 31, 2024.

After excluding these observations, the coefficient remains negative at −0.00681 with a p value of 0.026 and an R squared of 0.120.

For the 10 Year Treasury yield, the three observations with the highest Cook's distance are November 1, 2023, December 13, 2023, and July 31, 2024.

After excluding these observations, the coefficient is −0.00249 with a p value of 0.335 and an R squared of 0.020.

Thus, the 2 Year Treasury result remains statistically significant under the two day influence robustness specification, while the 10 Year Treasury result is no longer statistically significant.

## Robustness Summary

| Outcome | Window | Coefficient | P value | R squared | N |
|---|---|---:|---:|---:|---:|
| 2Y Treasury | 1 day | −0.00784 | 0.030 | 0.128 | 39 |
| 10Y Treasury | 1 day | −0.00679 | 0.016 | 0.141 | 39 |
| 2Y Treasury | 2 day | −0.00684 | 0.057 | 0.081 | 39 |
| 10Y Treasury | 2 day | −0.00636 | 0.043 | 0.093 | 39 |
| 2Y Treasury | 1 day, influence robust | −0.00563 | 0.029 | 0.082 | 36 |
| 10Y Treasury | 1 day, influence robust | −0.00568 | 0.044 | 0.099 | 36 |
| 2Y Treasury | 2 day, influence robust | −0.00681 | 0.026 | 0.120 | 36 |
| 10Y Treasury | 2 day, influence robust | −0.00249 | 0.335 | 0.020 | 36 |

## Interpretation

The results suggest that unexpected FOMC communication is associated with Treasury yield movements beyond the contemporaneous change in the Federal Funds Rate.

The strongest evidence appears in the announcement day response. Both the 2 Year and 10 Year Treasury yields show negative and statistically significant coefficients in the main specification. These results remain statistically significant after excluding the most influential observations.

The two day event window produces a similar pattern, although the evidence becomes weaker for the 10 Year Treasury yield after influential observations are excluded.

No statistically significant relationship is detected between unexpected FOMC communication and the VIX in the main specification.

The negative coefficient estimates should be interpreted cautiously. The communication measure is based on a dictionary approach, and the sample contains only 40 FOMC announcements. The analysis identifies statistical associations rather than causal effects.

Overall, the evidence suggests that FOMC statement language contains information associated with Treasury market movements, particularly around the announcement date and for the 2 Year Treasury yield.