# Empirical Results

## Research Question

This study examines whether the tone of Federal Open Market Committee (FOMC) statements is associated with movements in Treasury yields around monetary policy announcements.

## Data

The sample contains 40 FOMC statements from January 2021 through December 2024. Market data include 2 year Treasury yields, 10 year Treasury yields, the VIX index, and the Federal Funds Rate from FRED.

For each FOMC announcement, the market reaction is measured as the change between the last trading day before the announcement and the first trading day after the announcement.

## Communication Measure

FOMC statement language is classified using a dictionary based measure of hawkish and dovish terms. The resulting hawkishness measure is normalized by statement length.

To separate communication content from the contemporaneous policy rate movement, hawkishness is regressed on the change in the Federal Funds Rate. The residual from this regression is used as the unexpected communication component.

## Main Results

The regression results show a statistically significant association between unexpected FOMC communication and Treasury yield movements.

For the 2 year Treasury yield, the coefficient on unexpected tone is −0.00784 with a p value of 0.030. The model has an R squared of 0.128.

For the 10 year Treasury yield, the coefficient is −0.00679 with a p value of 0.016. The model has an R squared of 0.141.

For the VIX, the coefficient is 0.03155 with a p value of 0.544, indicating no statistically significant association between unexpected FOMC communication and the change in market volatility.

## Interpretation

The results suggest that FOMC statement language contains information associated with Treasury market movements beyond the contemporaneous change in the Federal Funds Rate. The association is statistically significant for both the 2 year and 10 year Treasury yields, while no statistically significant relationship is detected for the VIX.

The negative coefficient estimates should be interpreted cautiously because the communication measure is based on a dictionary approach and the sample contains only 40 FOMC announcements.

## Influence Robustness

An influence analysis based on Cook's distance identifies three observations with relatively high influence: the FOMC announcements of March 22, 2023, December 13, 2023, and March 16, 2022.

These observations are retained in the main specification because they represent genuine monetary policy events rather than data errors.

As a robustness check, the three observations are excluded and the 2 Year Treasury regression is re estimated using heteroskedasticity robust standard errors. The coefficient on unexpected communication remains negative at −0.00563 with a p value of 0.029, compared with −0.00784 and a p value of 0.030 in the full sample.

The persistence of the coefficient and statistical significance suggests that the main 2 Year Treasury result is not driven entirely by the most influential observations.

## 10 Year Treasury Influence Robustness

The same influence robustness test is applied to the 10 Year Treasury yield.

After excluding the three observations with the highest Cook's distance, the coefficient on unexpected communication remains negative at −0.00568 with a p value of 0.044. The coefficient is smaller than in the full sample, but statistical significance remains at the 5 percent level.

Taken together, the influence analysis suggests that the negative association between unexpected FOMC communication and Treasury yields is not driven entirely by a small number of influential observations.