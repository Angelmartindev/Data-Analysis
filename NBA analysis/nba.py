import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st
import datetime as dt

pd.set_option('max_columns', 20)
data = pd.read_csv('all_seasons.csv')

#we are going to set the season as an index
good_data = data.set_index('season')
good_data = good_data.drop(['Number'], axis=1) #Removing the first column (not neccesary)

#selecting data for that season in order to make the analisys for 2019-2020 season
data_2019_2020 = good_data.loc[['2019-20']]
(data_2019_2020.head())

#Here we can see standard statistics for the dataset
(data_2019_2020.describe())
(data_2019_2020.isna().sum()) #there are no missing values

#sns.relplot(data=data_2019_2020, x= 'age', y= 'pts', kind = 'line')
#plt.show()

#in this plot we can see that the range of age (25-30) is the more consistent talking about scoring.
#We also can see a pick of high scoring a 35, probably caused by players like lebron James (there are no
#many players with 35 or more years). After 35, scoring decreases drastically.
(data_2019_2020.loc[data_2019_2020['age'] == 35])

height_ranges = pd.cut(data_2019_2020.player_height,bins=[170,175,180,185,190,195,200,205,210,215,220,225],labels=['0-175','175-180','180-185','185-190',
                                                                             '190-195','195-200','200-205','205-210',
                                                                             '210-215','215-220','220+'
                                                                                                        ])
data_2019_2020.insert(5, 'players_height', height_ranges)

weight_ranges = pd.cut(data_2019_2020.player_weight, bins = [70,75,80,85,90,95,100,105,110,115,120,125,130], labels = ['70-75','75-80','80-85','85-90','90-95',
                                                                                                                   '95-100','100-105','105-110','110-115','115-120','125', '+125'])

data_2019_2020.insert(6, 'players_weight', weight_ranges)

sns.relplot(data = data_2019_2020, x=height_ranges, y=weight_ranges)
plt.gca().invert_yaxis()
plt.show()

#As it was expected, weight and height are correlated

sns.histplot(data_2019_2020['country'])
plt.show()

#The vast majority of the players are from USA
sns.relplot(data = data_2019_2020, x= height_ranges, y= data_2019_2020['reb'])
plt.show()

print(data_2019_2020['college'].value_counts())
#As we can see 123 active players in the season 2019-2020 didn´t go to college
#The universities that produced more active players (playing in 2019-2020 season were Kentucky and Duke)

#as we can see the players between 205-210 and 210-215 are the best rebounders. This means that not only the height is
#important to catch a rebound (athleticism is also important).

sns.relplot(data = data_2019_2020, x= height_ranges, y= data_2019_2020['pts'])
plt.show()

#In the rebounds graph, we can conclude something, but here is more difficult. There are no perfect height to score more points.
#It´s obvious that the smaller players have a lower scoring average, but avobe 190, we can see e a constant scoring average among the
#different ranges of height.

sns.relplot(x= data_2019_2020['reb'], y = data_2019_2020['pts'])
plt.show()

#rebounds include offensive and deffensive ones, so, we can see that there is a direct relation between points and rebounds with some
#exceptions (completely deffensive players like Rudy Gobbert).

sns.relplot(x= data_2019_2020['oreb_pct'], y = data_2019_2020['pts'])
sns.relplot(x= data_2019_2020['dreb_pct'], y = data_2019_2020['pts'])
plt.show()

#but talking about percentages while player is on the floor, the ones who score a lot of points are not the ones with higher oreb_pct or
#dreb_pct!

#a very important stat in basketball is the net_rating, which represents the team scoring differential per 100 possesions (while the player
#is on the court)

print(data_2019_2020.loc[(data_2019_2020['net_rating'] > 15) & (data_2019_2020['pts'] > 10)])

#As we can see, there was only 1 player with a net rating higher than 15 and scoring higher than 10. This is neccessary, cause there are players
#who had played only some minutes during the whole season and had scorings of 1 ,or 2 points per game in average, and thats not a real stat. The good stat would be
#comparing net_rating with minutes per game, but that variable is not included in this dataset.
#The player with those stats is obviously Giannis Antetokounmpo who also was the MVP of the regular season

#the player with the max value in each stat is
#we are going to change the index for the names to make the print easier
data_2019_2020 = data_2019_2020.set_index('player_name')

max_scorer = (data_2019_2020['pts'].idxmax())
max_score = max(data_2019_2020['pts'])
max_rebounder = (data_2019_2020['reb'].idxmax())
max_rebound = max(data_2019_2020['reb'])
max_assister = (data_2019_2020['ast'].idxmax())
max_assists = max(data_2019_2020['ast'])

print(f'The max scorer was {max_scorer} with {max_score} points')
print(f'The max rebounder was {max_rebounder} with {max_rebound} rebounds')
print(f'The max assisster was {max_assister} with {max_assists} assists')

