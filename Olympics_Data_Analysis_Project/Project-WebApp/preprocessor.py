import pandas as pd  # type: ignore
import helper


def preprocess( df,df_region):
    

    #Considering only Summer Olympics
    df = df[df['Season']=='Summer']
    #Merging the refion_df with df
    df = df.merge(df_region,on='NOC',how='left')
    #Drop Duplicates Values

    #print(df.columns) 

    df = df.drop_duplicates()
    #Doing One Hot Encoding on Medal
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)

    return df

# preprocess()
# helper.columns(df)







