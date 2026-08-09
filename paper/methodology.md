# Methodology

## 1. FOMC Statement Processing

The analysis uses 40 Federal Open Market Committee statements covering January 2021 through December 2024.

The raw statement text was cleaned to remove website navigation, headers, and other non statement content. The resulting text is stored in the processed FOMC dataset.

## 2. Communication Measure

A dictionary based communication measure is constructed from hawkish and dovish terms.

For each statement, the number of hawkish terms is compared with the number of dovish terms. The difference is normalized by the total number of words and scaled by 1,000:

$$
Hawkishness_i =
\frac{HawkishWords_i-DovishWords_i}
{TotalWords_i}
\times 1000
$$

A higher value represents relatively more hawkish language.

## 3. Unexpected Communication

The communication measure is strongly related to changes in the Federal Funds Rate. To separate communication content from the contemporaneous policy rate movement, hawkishness is regressed on the Federal Funds Rate change:

$$
Hawkishness_i =
\alpha+\beta DFFChange_i+\epsilon_i
$$

The residual $\epsilon_i$ is defined as unexpected communication.

This measure captures the component of statement language that is not explained by the contemporaneous Federal Funds Rate change.

## 4. Event Study

The main event window measures the change between the last trading day before the FOMC announcement and the first trading day after the announcement.

For Treasury yields:

$$
Reaction_i =
Yield_{i,+1}-Yield_{i,-1}
$$

The analysis considers both the 2 Year and 10 Year Treasury yields.

A two trading day window is also examined as a robustness test.

## 5. Regression Specification

The main regression specification is:

$$
Reaction_i =
\alpha+\beta UnexpectedTone_i+\epsilon_i
$$

The coefficient $\beta$ measures the association between unexpected FOMC communication and market reactions.

The analysis uses heteroskedasticity robust HC1 standard errors.

## 6. Influence Analysis

Cook's distance is used to identify observations that have relatively high influence on the regression estimates.

The three observations with the highest Cook's distance are excluded in a robustness specification. The main Treasury yield results remain statistically significant after this exclusion.

## 7. Interpretation

The empirical analysis is designed to identify statistical associations rather than causal effects. The relatively small sample of 40 FOMC announcements also motivates the use of multiple robustness checks and cautious interpretation of the estimated coefficients.