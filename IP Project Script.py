#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:59:10 2021

@author: jimmy
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


game = pd.read_csv('vgsales.csv').set_index('Rank')
score = pd.read_excel('Review Score.xlsx')
############ Data Exploration ################
sns.heatmap(game.isnull(), cbar=False)
sns.heatmap(score.isnull(), cbar=False)

game.info()
score.info()
# Drop missing values
game = game.dropna()


################## Genre by Region ###############

# Global sales
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', y = 'Global_Sales', data = game, estimator=sum)
plt.legend(title = 'Global Market',loc = "upper right")
plt.show()

# NA sales
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', y = 'NA_Sales', data = game, estimator=sum)
plt.legend(title = 'NA Market',loc = "upper right")
plt.show()

# EU sales
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', y = 'EU_Sales', data = game, estimator=sum)
plt.legend(title = 'EU Market',loc = "upper right")
plt.show()

# JP sales
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', y = 'JP_Sales', data = game, estimator=sum)
plt.legend(title = 'JP Market',loc = "upper right")
plt.show()

# Other sales
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', y = 'Other_Sales', data = game, estimator=sum)
plt.legend(title = 'Other Market',loc = "upper right")
plt.show()


###################### Publisher by Region #####################
game['Publisher'].value_counts() # 576 publisher in total

# Top publishers 
top_seller = game.groupby('Publisher').filter(lambda g:(g.Publisher.size >= 350))
top_seller['Publisher'].value_counts() # subset 24 publishers have size over 150


# Global sales
plt.figure(figsize=(10,5))
sns.barplot(x = 'Publisher', 
            y = 'Global_Sales', 
            data = top_seller, 
            estimator=sum,)
plt.legend(title = 'Global Market',loc = "upper right")
plt.xticks(fontsize=12, rotation=70)
plt.show()

# NA Sales
plt.figure(figsize=(10,5))
sns.barplot(x = 'Publisher', 
            y = 'NA_Sales', 
            data = top_seller, 
            estimator=sum,)
plt.legend(title = 'MA Market',loc = "upper right")
plt.xticks(fontsize=12, rotation=70)
plt.show()

# EU Sales
plt.figure(figsize=(10,5))
sns.barplot(x = 'Publisher', 
            y = 'EU_Sales', 
            data = top_seller, 
            estimator=sum,)
plt.legend(title = 'EU Market',loc = "upper right")
plt.xticks(fontsize=12, rotation=70)
plt.show()

# JP Sales
plt.figure(figsize=(10,5))
sns.barplot(x = 'Publisher', 
            y = 'JP_Sales', 
            data = top_seller, 
            estimator=sum,)
plt.legend(title = 'JP Market',loc = "upper right")
plt.xticks(fontsize=12, rotation=70)
plt.show()

# Other Sales
plt.figure(figsize=(10,5))
sns.barplot(x = 'Publisher', 
            y = 'Other_Sales', 
            data = top_seller, 
            estimator=sum,)
plt.legend(title = 'Other Market',loc = "upper right")
plt.xticks(fontsize=12, rotation=70)
plt.show()

################## Genre by Top Publishers ###############################

## Electronic Arts ##
EA = game[game['Publisher']=='Electronic Arts']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = EA.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Electronic Arts',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Activision ##
Activision = game[game['Publisher']=='Activision']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Activision.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Activision',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()

## Namco Bandai Games
Bandai = game[game['Publisher']=='Namco Bandai Games']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Bandai.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Namco Bandai Games',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Ubisoft
Ubisoft = game[game['Publisher']=='Ubisoft']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Ubisoft.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Ubisoft',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Konami Digital Entertainment
Konami = game[game['Publisher']=='Konami Digital Entertainment']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Konami.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Konami Digital Entertainment',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Konami Digital Entertainment
THQ = game[game['Publisher']=='THQ']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = THQ.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'THQ',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Nintendo ##
Nintendo = game[game['Publisher']=='Nintendo']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Nintendo.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Nintendo',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Sony Computer Entertainment
Sony = game[game['Publisher']=='Sony Computer Entertainment']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Sony.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Sony Computer Entertainment',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Sega
Sega = game[game['Publisher']=='Sega']

# Genre proportion
plt.figure(figsize=(10,5))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Sega.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Sega',loc = "upper right")
plt.xticks(fontsize=10, rotation=70)
plt.show()


## Take-Two Interactive
Take_Two = game[game['Publisher']=='Take-Two Interactive']

# Genre proportion
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Take_Two.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Take-Two Interactive',loc = "upper right")
plt.xticks(fontsize=10, rotation=0)
plt.show()


## Capcom
Capcom = game[game['Publisher']=='Capcom']

# Genre proportion
plt.figure(figsize=(15,8))
sns.barplot(x = 'Genre', 
            y = 'Global_Sales',
            data = Capcom.sort_values('Genre'), 
            estimator=sum,)
plt.legend(title = 'Capcom',loc = "upper right")
plt.xticks(fontsize=10, rotation=0)
plt.show()



# Inner join datasets 

# score dataset cleaning
score = score.rename(columns={'Game':'Name'})

# unify the Platform names
score['Platform'].value_counts()
game['Platform'].value_counts()

score['Platform'].loc[(score['Platform']== 'PlayStation 2')] = 'PS2'
score['Platform'].loc[(score['Platform']== 'PlayStation 3')] = 'PS3'
score['Platform'].loc[(score['Platform']== 'Wii U')] = 'WiiU'
score['Platform'].loc[(score['Platform']== 'PlayStation 4')] = 'PS4'
score['Platform'].loc[(score['Platform']== 'Nintendo DS')] = 'DS'
score['Platform'].loc[(score['Platform']== 'Xbox 360')] = 'X360'
score['Platform'].loc[(score['Platform']== 'Xbox One')] = 'XOne'
score['Platform'].loc[(score['Platform']== 'Xbox')] = 'XB'
score['Platform'].loc[(score['Platform']== 'Game Boy')] = 'GB'
score['Platform'].loc[(score['Platform']== 'Game Boy Advance')] = 'GBA'
score['Platform'].loc[(score['Platform']== 'GameCube')] = 'GC'
score['Platform'].loc[(score['Platform']== 'PlayStation Portable')] = 'PSP'
score['Platform'].loc[(score['Platform']== 'PlayStation')] = 'PS'
score['Platform'].loc[(score['Platform']== 'PlayStation Vita')] = 'PSV'
score['Platform'].loc[(score['Platform']== 'Nintendo 64')] = 'N64'
score['Platform'].loc[(score['Platform']== 'Super NES')] = 'SNES'
score['Platform'].loc[(score['Platform']== 'Atari 2600')] = '2600'


df_all = pd.merge(game, score,on = ['Name', 'Platform'], how='inner')
sns.heatmap(df_all.isnull(), cbar=False)

df_all.info()

# Final dataset cleaning
df_all = df_all.drop('Genre_y', axis = 1)

# Removing duplication from the dataset
df_final = df_all[~df_all[['Name', 'Platform']].apply(frozenset, axis=1).duplicated()]

# Create new variable Platform 2
df_final['Platform'].value_counts()
df_final['Master Platform'] = df_final['Platform']

# Nintendo Platform
df_final['Master Platform'].loc[df_final['Platform'] == 'Wii'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'DS'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'GC'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'GBA'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'N64'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'WiiU'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'NES'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'GB'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == '2600'] = 'Nintendo'
df_final['Master Platform'].loc[df_final['Platform'] == 'SNES'] = 'Nintendo'

# Sony Platform
df_final['Master Platform'].loc[df_final['Platform'] == 'PS2'] = 'Sony'
df_final['Master Platform'].loc[df_final['Platform'] == 'PS3'] = 'Sony'
df_final['Master Platform'].loc[df_final['Platform'] == 'PS'] = 'Sony'
df_final['Master Platform'].loc[df_final['Platform'] == 'PSP'] = 'Sony'
df_final['Master Platform'].loc[df_final['Platform'] == 'PSV'] = 'Sony'
df_final['Master Platform'].loc[df_final['Platform'] == 'PS4'] = 'Sony'

# Microsoft Platform
df_final['Master Platform'].loc[df_final['Platform'] == 'X360'] = 'Microsoft'
df_final['Master Platform'].loc[df_final['Platform'] == 'XB'] = 'Microsoft'
df_final['Master Platform'].loc[df_final['Platform'] == 'XOne'] = 'Microsoft'


# Unpiviot the dataset for visulization
df_final = df_final.melt(id_vars=['Name', 'Platform', 'Master Platform', 'Year', 'Genre_x', 'Publisher','Score'],
                   var_name='Region', 
                   value_name='Sales' )


# Assing region value
df_final['Region'].value_counts()


df_final['Market Region'] = df_final['Region']
df_final['Market Region'].loc[df_final['Region'] == 'NA_Sales'] = 'North America'
df_final['Market Region'].loc[df_final['Region'] == 'JP_Sales'] = 'Japan'
df_final['Market Region'].loc[df_final['Region'] == 'Global_Sales'] = 'Global'
df_final['Market Region'].loc[df_final['Region'] == 'EU_Sales'] = 'Europe'
df_final['Market Region'].loc[df_final['Region'] == 'Other_Sales'] = 'Other'




# Check NA again, the dataset is good to go
sns.heatmap(df_final.isnull(), cbar=False)
df_final.info()


# Write out csv file
df_final.to_excel('Game_Final.xlsx')




######################## Datasets Merging for IP2  ######################################

df1=pd.read_csv("playtime.csv")
df2=pd.read_csv("steam_games.csv")
df1.columns
df2.columns


##missisng values
sns.heatmap(df2.isnull(), cbar= False)
sns.heatmap(df1.isnull(), cbar= False)
##
df2.drop(['url','discount_price','recommended_requirements','mature_content','minimum_requirements','languages'],inplace=True,axis=1)
df2.rename(columns={'name':'Game Name'},inplace=True)
df2.columns

##keep relative columns 
df2=df2[["types","Game Name","all_reviews", "release_date","developer","publisher", "popular_tags","genre","original_price"]]

##extract reviews from dataset
#extract popular tags

##merge two datasets by game name
final = pd.merge(df1,df2,how='inner',left_on='Game Name',right_on='Game Name')
sns.heatmap(final.isnull(), cbar= False)

final.to_csv('final.csv', index=False)
#top 30 games played
topst = final.sort_values('Hours Played',ascending=False)[2:32]
topst












