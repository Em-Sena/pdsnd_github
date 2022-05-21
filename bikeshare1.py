import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    #lower is used to get input in any format

    while(True):
        if city in ('chicago', 'new york','washington','all'):
            break
        else:
            city = input('Enter Correct city: ').lower()
             #lower is used to get input in any format
    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month would you like to see data from? January, February, March, April, May, or June?\n').lower()
     #lower is used to get input in any format

    while(True):
        if month in ('january','february', 'march','april','may','june','all'):
            break
        else:
            month = input('Wrong input.Enter valid month\n').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Do you want data from monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n').lower()
     #lower is used to get input in any format
    while(True):

        if day in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            break
        else:
            day = input('Wrong entry!Enter Correct day: \n').lower()
             #lower is used to get input in any format

    #return day

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
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]

    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\nMost common start station is {}\n'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost common end station is {}\n'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_trip = combination_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time1 = total_travel_time
    day = time1 // (24 * 3600)
    time1 = time1 % (24 * 3600)
    hour = time1 // 3600
    time1 %= 3600
    minutes = time1 // 60
    time1 %= 60
    seconds = time1
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    time2 = avg_travel_time
    day2 = time2 // (24 * 3600)
    time2 = time2 % (24 * 3600)
    hour2 = time2 // 3600
    time2 %= 3600
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print('\nAverage travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nTotal Number of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('\nTotal Number of customers are {}\n'.format(int(no_of_customers)))

    # Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nTotal Number of male users are {}\n'.format(int(male_count)))
        print('\nTotal Number of female users are {}\n'.format(int(female_count)))


    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), int(most_common_birth_year)))
    #ask user if he wants to display raw data and print 5 rows at a time    
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    if view_data.lower() == 'yes':
        start_loc=0
        while True:
                print(df.iloc[start_loc:start_loc+5])
                start_loc=+5
                ask = input("Do you wish to continue with another 5 rows?: ").lower()
                if ask.lower()!='yes':
                    break
         
            
   
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
    #repos used 
    #https://github.com/nidhikapoor21/Explore-US-Bikeshare-Data/blame/master/bikeshare_2.py, https://github.com/khaledimad/Explore-US-Bikeshare-Data/blob/master/bikeshare_2.py#L108, https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206.

#https://appdividend.com/2019/01/28/python-mode-function-example-python-statistics-tutorial/#:~:text=The%20mode%20is%20a%20value,in%20a%20set%20of%20numbers.

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#
#https://github.com/YashMotwani/US-Bikeshare-Data-Exploration-Program/blob/master/bikeshare_2.py