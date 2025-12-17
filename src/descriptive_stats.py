EDA and Variable Understanding

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("/content/nssal_analysis_ready_with_age.csv")

# Preview data
df.head()

# Check data types and missing values
print(df.info())
print(df.isnull().sum())

# Value counts for categorical variables
print("Gender distribution:\n", df['rsex'].value_counts())
print("\nSurvey wave distribution:\n", df['wave'].value_counts())

# Descriptive stats for the number of partners
print("\nDescriptive statistics for hetlife_num:\n", df['hetlife_num'].describe())

# Plot histogram for hetlife_num
plt.figure(figsize=(8,5))
sns.histplot(df['hetlife_num'], bins=30, kde=True)
plt.title('Distribution of Number of Heterosexual Partners')
plt.xlabel('Number of Partners')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Boxplot to compare gender vs number of partners
plt.figure(figsize=(8,5))
sns.boxplot(x='rsex', y='hetlife_num', data=df)
plt.title('Number of Partners by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Partners')
plt.grid(True)
plt.show()

# Bar plot of gender and wave distributions
plt.figure(figsize=(6,4))
sns.countplot(x='rsex', hue='wave', data=df)
plt.title('Gender by Survey Wave')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Wave')
plt.show()


# interaction plot
sns.pointplot(x='wave', y='hetlife_num', hue='rsex', data=df, dodge=True, markers=['o', 's'], capsize=.1)
plt.title('Interaction: Gender × Wave on Number of Partners')
plt.xlabel('Survey Wave')
plt.ylabel('Number of Heterosexual Partners')
plt.legend(title='Gender')
plt.grid(True)
plt.show()
