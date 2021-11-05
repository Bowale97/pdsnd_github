import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago','new york city','washington']

months = ['all','january','february','march','april','may','june']

days = ['all','monday','tuesday','wednesday','thursday','friday','satuday','sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi!, looking to get some information?')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city are you interested in getting stats on? the options are 'chicago', 'new york city' or 'washington'\n").lower()

        if city in cities:
            break
        else:
            print('wrong entry!')


        # get user input for month (all, january, february, ... , june)
    while True:
        month = input('We have stats for the first 6 months of the year, are you interested in all or a specific month?\n').lower()

        if month in months:
            break
        else:
            print('ops!,check what you typed')

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('do you want stats for all the days?, if not specify what day you are interested in\n').lower()

        if day in days:
            break
        else:
            print('ops!,check what you typed')

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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Start hour']= df['Start Time'].dt.hour
   

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

def display_raw_data(df):
    ''' This would display the raw data on screen'''
    more=input("Do you want to see the first 5 rows of the data(yes or no)\n").lower()
    n=0
    while more == 'yes':
        n +=5
        print(df.iloc[n-5:n,:])
        more = input('do you want to see another set of rows?\n').lower()        
        
        
        
        
        
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    common_day = df['day_of_week'].value_counts().idxmax()
    common_hour = df['Start hour'].value_counts().idxmax()
    # display the most common month
    if month == all:
        print('The busiest month is \n {}'.format(common_month))
    # display the most common day of week
    if day == all:
        print('The busiest day is \n {}'.format(common_day))
    # display the most common start hour
    print('The busiest day is \n {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Hotspot = df['Start Station'].value_counts().idxmax()
    Endpoint = df['End Station'].value_counts().idxmax()
    print('The preferred departure station is \n {}'.format(Hotspot))
    # display most commonly used end station
    print('The most used end station is \n {}'.format(Endpoint))
    # display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station']+'-'+ df['End Station']
    common_route = df['Route'].value_counts().idxmax()
    print('The most common route is \n {}'.format(common_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

        # display total travel time
    Total_time = df['Trip Duration'].sum()
    print('Total Travel time: \n {}'.format(Total_time))

        # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Average travel time: \n {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('This is the count of the user types {}'.format(user_types))
        # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('The gender distribution of customers are: {}'.format(gender))
        # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        print('the birth year of the oldest customer is {}'.format(earliest))
        most_recent = int(df['Birth Year'].max())
        print('the birth year of the youngest customer is {}'.format(most_recent))
        common_year = int(df['Birth Year'].mode())
        print('the most common birth year is {}'.format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
