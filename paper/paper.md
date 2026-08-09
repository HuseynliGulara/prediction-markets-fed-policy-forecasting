# Fed Language and Financial Markets

## Abstract

This study examines the relationship between the tone of Federal Open Market Committee statements and financial market reactions around monetary policy announcements. The analysis uses 40 FOMC statements from January 2021 through December 2024 and combines natural language processing, event study methods, and ordinary least squares regression.

A dictionary based hawkishness measure is constructed from the language of each FOMC statement. To separate communication content from contemporaneous monetary policy changes, the hawkishness measure is regressed on the change in the Federal Funds Rate. The residual from this regression is interpreted as unexpected FOMC communication.

The results show a statistically significant negative association between unexpected communication and both 2 Year and 10 Year Treasury yield reactions during the announcement day window. The coefficient is −0.00784 for the 2 Year Treasury yield with a p value of 0.030 and −0.00679 for the 10 Year Treasury yield with a p value of 0.016. No statistically significant relationship is found for the VIX.

The results remain broadly consistent after influential observations are excluded. The strongest evidence is concentrated in Treasury yields and particularly in the announcement day response.

## 1. Introduction

Central bank communication plays an important role in financial markets. Monetary policy announcements contain information about current policy decisions as well as information about the Federal Reserve's assessment of economic and financial conditions.

Financial market participants therefore respond not only to changes in the Federal Funds Rate but also to the language used by the Federal Open Market Committee.

This study examines the relationship between FOMC statement language and financial market reactions around monetary policy announcements. The analysis focuses on Treasury yields and market volatility.

The main research question is:

> Does the tone of FOMC statements contain information associated with subsequent movements in Treasury yields and market volatility?

The analysis focuses on three market outcomes: the 2 Year Treasury yield, the 10 Year Treasury yield, and the VIX index.

The central empirical challenge is separating the information contained in FOMC communication from the contemporaneous policy rate decision. A statement may appear more hawkish because the Federal Funds Rate increased at the same announcement. To address this issue, the analysis removes the component of the hawkishness measure explained by the contemporaneous Federal Funds Rate change.

The resulting residual is interpreted as the unexpected communication component.

The empirical results indicate a negative and statistically significant association between unexpected FOMC communication and Treasury yield reactions during the announcement day window. The evidence for the VIX is not statistically significant.

The findings should be interpreted as statistical associations rather than causal effects.

## 2. Data

The sample contains 40 FOMC statements from January 2021 through December 2024.

The analysis combines FOMC statement data with financial market data obtained from the Federal Reserve Bank of St. Louis FRED database.

The market variables are:

1. 2 Year Treasury yield
2. 10 Year Treasury yield
3. VIX index
4. Federal Funds Rate

The FOMC announcement dates are matched with the corresponding market observations.

For each announcement, the market reaction is calculated relative to the FOMC announcement date.

The main event window compares the last trading day before the announcement with the first trading day after the announcement.

A two trading day window is also examined as a robustness specification.

## 3. FOMC Statement Processing

The FOMC statements are processed using Python.

The text is cleaned before calculating the communication measure. Non statement content is removed and the remaining text is converted into a consistent format for text analysis.

The cleaned statements are then analyzed using dictionaries containing hawkish and dovish terms.

The purpose of this procedure is to construct a transparent and reproducible measure of the tone of FOMC communication.

## 4. Communication Measure

The primary communication measure is a hawkishness score.

For each statement, the number of hawkish terms and the number of dovish terms are counted.

The score is defined as:

$$
Hawkishness_i =
\frac{HawkishWords_i - DovishWords_i}
{TotalWords_i}
\times 1000
$$

The normalization by total statement length prevents longer statements from mechanically receiving larger scores.

Higher values indicate a greater relative presence of hawkish language.

The resulting measure varies across FOMC announcements and provides a quantitative measure of communication tone.

## 5. Unexpected FOMC Communication

The main empirical challenge is distinguishing communication from the contemporaneous monetary policy decision.

A more hawkish statement may occur at the same time as an increase in the Federal Funds Rate. If the hawkishness measure were used without adjustment, the estimated relationship with market reactions could partly reflect the policy rate decision itself.

To address this issue, hawkishness is regressed on the contemporaneous change in the Federal Funds Rate:

$$
Hawkishness_i =
\alpha +
\gamma DFFChange_i +
u_i
$$

The residual from this regression is defined as unexpected communication:

$$
UnexpectedTone_i = u_i
$$

This measure captures the component of statement tone that is not explained by the contemporaneous Federal Funds Rate change.

The correlation between hawkishness and the Federal Funds Rate change is approximately 0.651, indicating a meaningful relationship between the communication measure and policy rate movements.

Using the residual therefore provides a way to separate the communication component from the contemporaneous policy rate movement.

## 6. Event Study Design

The event study examines financial market movements around FOMC announcements.

For the main specification, the event reaction is calculated as:

$$
Reaction_i =
MarketValue_{after,i}
-
MarketValue_{before,i}
$$

The main event window uses the last trading day before the announcement and the first trading day after the announcement.

Three market reactions are examined:

1. 2 Year Treasury yield reaction
2. 10 Year Treasury yield reaction
3. VIX reaction

A two trading day event window is also examined as a robustness test.

The purpose of the second window is to examine whether the estimated relationship persists beyond the immediate announcement response.

## 7. Regression Specification

The main regression specification is:

$$
Reaction_i =
\alpha +
\beta UnexpectedTone_i +
\epsilon_i
$$

where:

$$
Reaction_i
$$

represents the market reaction around the FOMC announcement.

The variable:

$$
UnexpectedTone_i
$$

represents the residual component of FOMC hawkishness after controlling for the contemporaneous Federal Funds Rate change.

The coefficient of interest is:

$$
\beta
$$

A negative coefficient indicates that higher unexpected communication is associated with a more negative market reaction.

All main regression specifications use heteroskedasticity robust HC1 standard errors.

The analysis focuses on statistical association rather than causal identification.

## 8. Main Results

The main results show a statistically significant negative association between unexpected FOMC communication and Treasury yield reactions.

For the 2 Year Treasury yield, the coefficient on unexpected tone is −0.00784 with a p value of 0.030. The R squared is 0.128 and the specification contains 39 observations.

For the 10 Year Treasury yield, the coefficient is −0.00679 with a p value of 0.016. The R squared is 0.141 and the specification contains 39 observations.

For the VIX, the coefficient is 0.03155 with a p value of 0.544. The R squared is 0.008.

The Treasury results indicate a statistically significant association between unexpected FOMC communication and Treasury yield movements.

The VIX result does not provide statistically significant evidence of an association between unexpected communication and market volatility.

## 9. Two Day Event Window Results

The two trading day event window produces similar negative coefficient estimates for both Treasury yields.

For the 2 Year Treasury yield, the coefficient is −0.00684 with a p value of 0.057 and an R squared of 0.081.

For the 10 Year Treasury yield, the coefficient is −0.00636 with a p value of 0.043 and an R squared of 0.093.

The 2 Year estimate is close to conventional statistical significance but does not reach the 5 percent level.

The 10 Year estimate remains statistically significant at the 5 percent level.

These findings suggest that the negative relationship observed in the announcement day window can also appear over a slightly longer event window, although the strength of the evidence differs across maturities.

## 10. Influence Analysis

Cook's distance is used to identify observations that have relatively high influence on the regression estimates.

The influence analysis is conducted separately for the different specifications.

For the one day 2 Year Treasury specification, the observations with the highest Cook's distance include the FOMC announcements of March 16, 2022, March 22, 2023, and December 13, 2023.

For the one day 10 Year Treasury specification, influential observations include November 1, 2023, December 13, 2023, and July 31, 2024.

These observations are retained in the main specification because they represent genuine monetary policy events rather than data errors.

The influence analysis is therefore used as a robustness exercise rather than as a justification for removing observations from the primary sample.

## 11. Influence Robustness Results

The three observations with the highest Cook's distance are excluded from each specification as a robustness test.

For the one day 2 Year Treasury specification, the coefficient on unexpected tone becomes −0.00563 with a p value of 0.029 and an R squared of 0.082.

For the one day 10 Year Treasury specification, the coefficient becomes −0.00568 with a p value of 0.044 and an R squared of 0.099.

The coefficients remain negative and statistically significant.

The two day influence robustness specification produces a coefficient of −0.00681 for the 2 Year Treasury yield with a p value of 0.026 and an R squared of 0.120.

For the 10 Year Treasury yield, the corresponding coefficient is −0.00249 with a p value of 0.335 and an R squared of 0.020.

The two day 2 Year Treasury result therefore remains statistically significant after excluding influential observations, while the two day 10 Year Treasury result becomes statistically insignificant.

## 12. Summary of Empirical Evidence

The empirical evidence can be summarized across the different specifications.

The main announcement day specification produces statistically significant negative coefficients for both Treasury maturities.

The 2 Year Treasury coefficient is −0.00784 with a p value of 0.030.

The 10 Year Treasury coefficient is −0.00679 with a p value of 0.016.

The two day specification produces coefficients of −0.00684 for the 2 Year Treasury yield and −0.00636 for the 10 Year Treasury yield.

After influential observations are excluded, the one day coefficients remain negative and statistically significant for both Treasury maturities.

The two day 2 Year Treasury result also remains statistically significant, while the corresponding 10 Year Treasury estimate does not.

The VIX specification does not produce statistically significant evidence of a relationship with unexpected FOMC communication.

Taken together, the strongest evidence is concentrated in Treasury yields and particularly in the announcement day response.

## 13. Interpretation

The results suggest that FOMC statement language contains information associated with Treasury market movements beyond the contemporaneous change in the Federal Funds Rate.

The negative coefficient estimates indicate that higher unexpected communication scores are associated with negative movements in the measured Treasury yield reactions.

The relationship is observed for both the 2 Year and 10 Year Treasury yields in the main announcement day specification.

The 2 Year Treasury result is particularly persistent across the robustness specifications.

The evidence for the 10 Year Treasury yield is also statistically significant in the main announcement day specification and in the two day full sample specification, but becomes weaker after influential observations are excluded from the two day specification.

The lack of statistical significance for the VIX suggests that the communication measure has a more detectable relationship with Treasury yields than with broad market volatility in this sample.

## 14. Limitations

Several limitations should be considered when interpreting the results.

First, the sample contains only 40 FOMC announcements. This limits statistical power and makes individual observations potentially important for the estimated coefficients.

Second, the communication measure is based on a dictionary approach. Dictionary based measures can capture the frequency of selected words but may not fully capture context, negation, sentence structure, or changes in the meaning of language.

Third, the unexpected communication measure is constructed using the Federal Funds Rate change. Other components of monetary policy information may also affect FOMC language and market reactions.

Fourth, the event study measures market reactions over relatively short windows. These windows reduce the influence of unrelated market developments but may not capture information that is incorporated into prices over a longer period.

Finally, the regressions identify statistical associations rather than causal effects. The results should therefore not be interpreted as evidence that FOMC communication independently causes Treasury yield movements.

## 15. Conclusion

This study examines the relationship between FOMC statement language and financial market reactions around monetary policy announcements.

Using a dictionary based hawkishness measure and an unexpected communication component constructed from Federal Funds Rate changes, the analysis finds a statistically significant negative association between unexpected FOMC communication and both 2 Year and 10 Year Treasury yield reactions in the main announcement day specification.

The relationship remains statistically significant after influential observations are excluded for the one day Treasury specifications.

The two day analysis provides additional evidence for the 2 Year Treasury yield, while the evidence for the 10 Year Treasury yield becomes weaker after influential observations are removed.

No statistically significant relationship is detected between unexpected FOMC communication and the VIX.

Overall, the results are consistent with FOMC statement language containing information associated with Treasury market movements beyond the contemporaneous policy rate change. The evidence is strongest for Treasury yields around the announcement date and for the 2 Year Treasury yield.

The findings should be interpreted cautiously given the small sample size, the dictionary based communication measure, and the observational nature of the analysis.