import pandas as pd

# Step 1: Read the raw .dta files
df1 = pd.read_stata("*******")
df2 = pd.read_stata("*******")


#
df1 = df1[['rsex', 'dage', 'dateyoi', 'hetlife', 'hettot', 'final_wt']].copy()
df1.rename(columns={'final_wt': 'weight'}, inplace=True)
df1['wave'] = 0  # NSSAL-2000

# 
df2 = df2[['rsex', 'dage', 'dateyoi', 'hetlife', 'hettot', 'total_wt']].copy()
df2.rename(columns={'total_wt': 'weight'}, inplace=True)
df2['wave'] = 1  # NSSAL-2010

# Step 3: Combine datasets from both waves
df = pd.concat([df1, df2], ignore_index=True)

# Step 4: Standardize gender values
df['rsex'] = df['rsex'].str.strip().str.lower()

# Step 5: Convert numeric values
partner_map = {
    '0': 0, '1': 1, '2': 2, '3': 3, '3-4': 3.5,
    '5': 5, '5-9': 7, '10+': 10, '12': 12, '15': 15, '20': 20
}
df['hetlife'] = df['hetlife'].astype(str)
df['hettot'] = df['hettot'].astype(str)
df['hetlife_num'] = df['hetlife'].map(partner_map)
df['hettot_num'] = df['hettot'].map(partner_map)

# Step 6: Create a clean subset for analysis
df_clean = df[['rsex', 'wave', 'dage', 'hetlife_num', 'weight']].copy()

# Step 7: Encode gender as numeric (0 = female, 1 = male)
df_clean['rsex_num'] = df_clean['rsex'].map({'female': 0, 'male': 1})

# Step 8: Drop missing values and reset index
df_clean.dropna(subset=['rsex_num', 'hetlife_num', 'weight', 'dage'], inplace=True)
df_clean.reset_index(drop=True, inplace=True)

# Step 9: CSV for download
df_clean.to_csv("/content/nssal_analysis_ready_with_age.csv", index=False)

# Optional: Preview
df_clean.head()
