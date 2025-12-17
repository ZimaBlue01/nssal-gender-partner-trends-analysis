# PART 2 – Week 2: Skewness, Transformation, Correlation

import numpy as np
from scipy.stats import skew, pearsonr, spearmanr
import matplotlib.pyplot as plt
import seaborn as sns

# Check skewness of hetlife_num
het_skew = skew(df['hetlife_num'].dropna())
print(f"Skewness of 'hetlife_num': {het_skew:.3f}")

# Histogram before transformation
plt.figure(figsize=(8,4))
sns.histplot(df['hetlife_num'], bins=30, kde=True)
plt.title('Original Distribution of Heterosexual Partners')
plt.xlabel('Number of Partners')
plt.ylabel('Frequency')
plt.show()

# Apply log10 transformation (add 1 to avoid log(0))
df['hetlife_log'] = np.log10(df['hetlife_num'] + 1)

# Histogram after transformation
plt.figure(figsize=(8,4))
sns.histplot(df['hetlife_log'], bins=30, kde=True, color='orange')
plt.title('Log10-Transformed Distribution of Heterosexual Partners')
plt.xlabel('Log10(Number of Partners + 1)')
plt.ylabel('Frequency')
plt.show()

# Pearson correlation (only if both variables are normal-ish)
pearson_corr, pearson_p = pearsonr(df['dage'], df['hetlife_num'])
print(f"Pearson correlation between age and number of partners: r = {pearson_corr:.3f}, p = {pearson_p:.4f}")

# Spearman correlation (non-parametric)
spearman_corr, spearman_p = spearmanr(df['dage'], df['hetlife_num'])
print(f"Spearman correlation between age and number of partners: r = {spearman_corr:.3f}, p = {spearman_p:.4f}")
