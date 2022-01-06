import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all' ]
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city = input("\npick a city from [ New York City, Chicago or Washington ]\n")
      city = city.lower()
      if city in ('New York City', 'Chicago', 'Washington'):
	break
      else:
        print("undefined answer, Try again")
        continue

    # get user input for month (all, january, february, ... , june)
    while True:
      month = input("\npick a month from [ January : June ] or type 'all'\n")
      month = month.lower()
      if month in MONTHS:
        break
      else:
        print("undefined answer, Try again")
        continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\npick a day from [ Monday : Sunday ] or type 'all'\n")
      day = day.lower()
      if day in DAYS:
        break
      else:
        print("undefined answer, Try again")
        continue
       

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day if applicable
    if day != 'all':

        # filter by day to create the new dataframe
        df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_mon = df['month'].mode()[0]
    print('Most Common Month is : ', common_mon)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day is : ', common_day)

    # display the most common start hour
    common_hour = (df['Start Time'].dt.hour).mode()[0]
    print('Most Common hour is : ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nMost Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station is : ', Start_Station)

    # display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station is : ', End_Station)

    # display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip is : ')
    print( Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel_time = int(df['Trip Duration'].sum())
    print('Total travel time:', Total_travel_time/86400, " Days")

    # display mean travel time
    Mean_travel_time = int(df['Trip Duration'].mean())
    print('Mean travel time:', Mean_travel_time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
      User_types = df['User Type'].value_counts()
      print('User Types is : \n', User_types)
    except KeyError:
      print("\nFor user types :\nNo data avaliable.")

    # Display counts of gender
    if 'Gender' in df:
      gender = df['Gender'].value_counts()
      print('\nGender Types is : \n', gender)
    else:
      print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # Display earliest, most recent, and most common year of birth
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year is : ', Earliest_Year)

      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year is : ', Most_Recent_Year)

      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year is : ', Most_Common_Year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	
     x = 1
    while True:
        raw = input('\nWould you like to see another trips? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
