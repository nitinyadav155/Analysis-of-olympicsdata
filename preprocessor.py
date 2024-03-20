import pandas as pd
def preprocess(df,region_df):
    # filtering the summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # adding medals name column in df
    df = pd.concat([df, pd.get_dummies(df['Medal'], dtype=int)], axis=1)
    return df