import numpy as np
import pandas as pd

# --------------------------------------------------------------
# Read CSV files
# --------------------------------------------------------------

drivers = pd.read_csv('../../data/raw/drivers.csv')
drivers_standings = pd.read_csv('../../data/raw/driver_standings.csv')
races = pd.read_csv('../../data/raw/races.csv')
results = pd.read_csv('../../data/raw/results.csv')
constructor = pd.read_csv('../../data/raw/constructors.csv')
constructor_standings = pd.read_csv('../../data/raw/constructor_standings.csv')


# --------------------------------------------------------------
# 1. Driver age analysis
# --------------------------------------------------------------
# --------------------------------------------------------------
# 1.1. Analyzing the age of drivers at the time of debut and at 
# the time of first win in Grand Prix.
# --------------------------------------------------------------

name_and_dob = drivers
name_and_dob['fullName'] = name_and_dob[['forename', 'surname']].agg(' '.join, axis=1)
name_and_dob = name_and_dob.drop(['url','nationality', 'driverRef', 'number', 'code', 'forename', 'surname'], axis=1)
name_and_dob[['driverId', 'fullName', 'dob']]

races_simplified = races[['raceId', 'name', 'date']]

races_results = pd.merge(pd.merge(drivers_standings,races_simplified,on='raceId'),name_and_dob,on='driverId',how='outer')
races_results = races_results[['fullName', 'dob', 'raceId', 'date', 'wins']]

drivers_debuts = races_results.groupby('fullName').agg({
    'dob': 'first',
    'date': lambda date: date.min()
}).reset_index()

drivers_first_win = races_results[races_results['wins'] == 1].groupby('fullName').agg({
    'dob': 'first',
     'date': lambda date: date.min()                     
}).reset_index()

drivers_debuts = drivers_debuts.rename(columns={'date':'debutDate'})
drivers_first_win = drivers_first_win.rename(columns={'date':'firstWinDate'})

debuts_and_win = pd.merge(drivers_debuts,drivers_first_win,on='fullName')

debuts_and_win = debuts_and_win.drop('dob_y', axis=1).rename(columns={'dob_x':'birthDate'})

debuts_and_win['birthDate'] = pd.to_datetime(debuts_and_win['birthDate'])
debuts_and_win['debutDate'] = pd.to_datetime(debuts_and_win['debutDate'])
debuts_and_win['firstWinDate'] = pd.to_datetime(debuts_and_win['firstWinDate'])


def calculate_age(birthDate, date):
    if not pd.isnull(date):
        age = (date-birthDate) / np.timedelta64(1, 'Y')
        return age
    else:
        return None
    
debuts_and_win["debutAge"] = debuts_and_win[["birthDate", "debutDate"]].apply(lambda df: calculate_age(df["birthDate"], df["debutDate"]), axis=1).apply(np.floor)
debuts_and_win["firstWinAge"] = debuts_and_win[["birthDate", "firstWinDate"]].apply(lambda df: calculate_age(df["birthDate"], df["firstWinDate"]), axis=1).apply(np.floor)

# test = debuts_and_win[debuts_and_win['fullName'] == 'Michael Schumacher']

debuts_and_win = debuts_and_win.sort_values("firstWinAge").set_index('fullName')

debuts_and_win.to_csv('../../data/processed/debuts_and_win.csv')

# --------------------------------------------------------------
# 1.2. Analyzing the average age of drivers in various periods 
# between 1950 and 2023.
# --------------------------------------------------------------

races_years = races[['raceId', 'year', 'date']]

def calculate_period(year):
    if year >= 2020:
        return 8
    elif year >= 2010 and year < 2020:
        return 7
    elif year >= 2000 and year < 2010:
        return 6
    elif year >= 1990 and year < 2000:
        return 5
    elif year >= 1980 and year < 1990:
        return 4
    elif year >= 1970 and year < 1980:
        return 3
    elif year >= 1960 and year < 1970:
        return 2
    else:
        return 1
    
races_years['period'] = races_years['year'].apply(calculate_period)

races_period = pd.merge(pd.merge(races_years,drivers_standings,on='raceId'),drivers,on='driverId')

races_period = races_period[['raceId','year', 'date','period','driverId', 'dob']]

races_period['date'] = pd.to_datetime(races_period['date'])
races_period['dob'] = pd.to_datetime(races_period['dob'])   

races_period["age"] = races_period[["date", "dob"]].apply(lambda df: calculate_age(df["dob"], df["date"]), axis=1).apply(np.floor)

races_period = races_period[['raceId','period', 'year','age']]

avg_drivers_age = races_period.groupby('period').agg({
    'year': ['median'],
    'age': 'mean'
}).reset_index(level=0)

avg_drivers_age['age'] = avg_drivers_age['age'].round(1)

avg_drivers_age = avg_drivers_age.droplevel(0, axis=1)

avg_drivers_age = avg_drivers_age.rename(columns={'median': 'year','mean': 'ageMean'})

avg_drivers_age['year'] = avg_drivers_age['year'].astype(int)

avg_drivers_age.info()

avg_drivers_age.to_csv('../../data/processed/avg_drivers_age.csv')

# --------------------------------------------------------------
# 2. Drivers from different countries
# --------------------------------------------------------------
# --------------------------------------------------------------
# 2.1. Analyzing the achievements of drivers from different countries.
# --------------------------------------------------------------

country_standings_wins = pd.merge(drivers,drivers_standings,on='driverId').groupby('nationality').sum().reset_index()

country_standings_wins = country_standings_wins[['nationality', 'wins', 'points']].sort_values(['wins', 'points'], ascending=False).reset_index(drop=True)

country_standings_wins.to_csv('../../data/processed/country_standings_wins.csv')

# --------------------------------------------------------------
# 2.2. Identifying the dominant nationalities in Formula 1.
# --------------------------------------------------------------

country_standings_drivers = drivers.groupby('nationality')['driverId'].count().sort_values(ascending=False)

# --------------------------------------------------------------
# 3. Analysis of driver's careers
# --------------------------------------------------------------
# --------------------------------------------------------------
# 3.1. Analyzing the length of driver's careers in Formula 1.
# --------------------------------------------------------------

careers_length = pd.merge(pd.merge(drivers, drivers_standings, on='driverId', how='outer'), races, on='raceId', how='outer')

careers_length = careers_length[['fullName', 'date']]

careers_length['date'] = pd.to_datetime(careers_length['date'])

careers_length = careers_length.groupby('fullName').agg({
    'date': ['min', 'max']
}).reset_index()

careers_length.info()

careers_length['career_len'] = careers_length['date']['max'] - careers_length['date']['min']

careers_length.sort_values('career_len', ascending=False)

careers_length.to_csv('../../data/processed/careers_length.csv')

# --------------------------------------------------------------
# 3.2. Identification of drivers who have spent their entire 
# career with one team.
# --------------------------------------------------------------

drivers_teams = results[['driverId', 'constructorId']]

drivers_teams = drivers_teams.drop_duplicates(
  subset = ['driverId', 'constructorId'],
  keep = 'last').reset_index(drop = True)

drivers_teams = pd.merge(pd.merge(drivers_teams,drivers,on='driverId'),constructor,on='constructorId')[['fullName', 'name']]

drivers_teams['teams_number'] = drivers_teams.groupby('fullName')['name'].transform('count')

one_team_drivers = drivers_teams[['fullName', 'teams_number', 'name']][drivers_teams['teams_number'] == 1]

# --------------------------------------------------------------
# 4. Multiple champion drivers
# --------------------------------------------------------------
# --------------------------------------------------------------
# 4.1. Analysis of drivers who have won the Formula 1 championship 
# more than once.
# --------------------------------------------------------------

races_results = pd.merge(results,races,on='raceId')[['driverId', 'points', 'year']]

races_results = races_results.groupby(['year', 'driverId']).sum().reset_index()

races_results = races_results[races_results['points'] == races_results.groupby(['year'])['points'].transform('max')].reset_index(drop=True)

seson_winners = pd.merge(races_results,drivers,on='driverId')[['year','points', 'fullName']].sort_values('year')

number_of_wins = seson_winners.groupby('fullName').size().reset_index(name='winsNumber').sort_values('winsNumber',ascending=False)

# --------------------------------------------------------------
# 4. Team changes
# --------------------------------------------------------------
# --------------------------------------------------------------
# 4.1. The impact of changing teams on driver's mean points 
# results per race.
# --------------------------------------------------------------

drivers_results = results[['driverId', 'constructorId', 'points', 'raceId']]

drivers_results = pd.merge(pd.merge(pd.merge(drivers_results,drivers,on='driverId'),constructor,on='constructorId'), races, on='raceId')

drivers_results = drivers_results[['fullName', 'name_x', 'points', 'date']]

drivers_results = drivers_results.rename(columns={'name_x': 'constructorName'})

drivers_results = drivers_results.groupby(['fullName', 'constructorName']).agg({
    'points': 'mean',
    'date': 'last'
}).reset_index()

drivers_results.sort_values(by=['fullName', 'date'], inplace=True)

drivers_results = drivers_results[['fullName', 'constructorName', 'points']]

# test4 = drivers_results[drivers_results['fullName'] == 'Michael Schumacher'] 