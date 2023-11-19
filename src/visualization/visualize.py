import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------
# 1. Driver age analysis
# --------------------------------------------------------------
# --------------------------------------------------------------
# 1.1. Analyzing the age of drivers at the time of debut and at 
# the time of first win in Grand Prix.
# --------------------------------------------------------------

debut_and_win = pd.read_csv('../../data/processed/debuts_and_win.csv')

plt.figure(figsize=(14,8), dpi=200)
sns.scatterplot(debut_and_win,x='debutAge', y='firstWinAge', s=140)

plt.figure(figsize=(14,8), dpi=200)
plt.xlim(10,60)
sns.kdeplot(debut_and_win[['debutAge','firstWinAge']], fill=True)

# --------------------------------------------------------------
# 1.2. Analyzing the average age of drivers in various periods 
# between 1950 and 2023.
# --------------------------------------------------------------

avg_drivers_age = pd.read_csv('../../data/processed/avg_drivers_age.csv')

plt.figure(figsize=(14,8), dpi=200)
plt.xlim(1950, 2050)
sns.barplot(avg_drivers_age,x='year',y='ageMean')

# --------------------------------------------------------------
# 2. Drivers from different countries
# --------------------------------------------------------------
# --------------------------------------------------------------
# 2.1. Analyzing the achievements of drivers from different countries.
# --------------------------------------------------------------

country_standings_wins = pd.read_csv('../../data/processed/country_standings_wins.csv')

country_standings_wins = country_standings_wins[['nationality','wins','points']]

country_standings_wins_wins = country_standings_wins.nlargest(10, 'wins')
country_standings_wins_points = country_standings_wins.nlargest(10, 'points')

plt.figure(figsize=(14,8), dpi=200)
plt.title('Most wins - country')
sns.barplot(country_standings_wins_wins, x='nationality', y='wins')

plt.figure(figsize=(14,8), dpi=200)
plt.title('Most points - country')
sns.barplot(country_standings_wins_points, x='nationality', y='points')

# --------------------------------------------------------------
# 3. Analysis of driver's careers
# --------------------------------------------------------------
# --------------------------------------------------------------
# 3.1. Analyzing the length of driver's careers in Formula 1.
# --------------------------------------------------------------

careers_length = pd.read_csv('../../data/processed/careers_length.csv')

careers_length = careers_length[['fullName', 'career_len']].tail(-1)

careers_length['career_len'] = careers_length['career_len'].str.extract('(^\d*)')

careers_length['career_len'] = careers_length['career_len'].astype(str)

careers_length = careers_length[careers_length["career_len"].str.contains("nan") == False] 

careers_length['career_len'] = careers_length['career_len'].astype(int)

careers_length = careers_length.nlargest(10,'career_len')

plt.figure(figsize=(20,8), dpi=200)
plt.title('The longest careers')
sns.barplot(careers_length, x='fullName', y='career_len')