from scipy.stats import ttest_ind, levene
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import shapiro
import pingouin as pg

# Drop rows with missing values in relevant columns
df_clean = df.dropna(subset=['hetlife_num', 'rsex', 'dage'])

# ---- T-TEST: Gender Differences ----
# Split into two groups
male_partners = df_clean[df_clean['rsex'] == 'male']['hetlife_num']
female_partners = df_clean[df_clean['rsex'] == 'female']['hetlife_num']

# Levene’s test for homogeneity of variance
stat, p_levene = levene(male_partners, female_partners)
print(f"Levene’s Test for Equal Variance: stat = {stat:.3f}, p = {p_levene:.4f}")

# Independent samples t-test
t_stat, p_value = ttest_ind(male_partners, female_partners, equal_var=p_levene > 0.05)
print(f"T-test for gender difference: t = {t_stat:.3f}, p = {p_value:.4f}")

# ---- LINEAR REGRESSION: Age → hetlife_num ----
# Use log-transformed version because of skewness
model = smf.ols('hetlife_num ~ dage', data=df_clean).fit()

# Summary
print(model.summary())

# Residual normality check
shapiro_test = shapiro(model.resid)
print(f"\nShapiro-Wilk test for residual normality: stat = {shapiro_test.statistic:.3f}, p = {shapiro_test.pvalue:.4f}")

# ---- TWO-WAY ANOVA: Gender and Wave ----
# Drop missing values for ANOVA
df_anova = df.dropna(subset=['hetlife_num', 'rsex', 'wave'])

# Levene’s Test (homogeneity of variance)
stat, p = levene(
    df_anova[df_anova['rsex'] == 'male']['hetlife_num'],
    df_anova[df_anova['rsex'] == 'female']['hetlife_num']
)
print(f"\nLevene’s Test (ANOVA): stat = {stat:.3f}, p = {p:.4f}")

# Two-way ANOVA model using pingouin for effect size
aov_pg = pg.anova(dv='hetlife_num', between=['rsex', 'wave'], data=df_anova, detailed=True)
print("\nPingouin ANOVA Table with Effect Sizes:\n", aov_pg)
