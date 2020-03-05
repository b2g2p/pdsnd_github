import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    cities = ['Chicago', 'New York City', 'Washington']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

    print('Hello! Let\'s explore some US bikeshare data today!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
        city = (input("Select city from Chicago, New York City, Washington: "))
        if city.title() not in cities:
            print("Invalid entry. Please select from the options provided.")
        else:

            break

        # get user input for month (all, january, february, ... , june)

    while True:
        month = input("Select month from January, February, March, April, May, June, All: ")
        if month.title() not in months:
            print("Invalid entry. Please select from the options provided.")
        else:

            break



        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Select Day of the Week from: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All: ")
        if day.title() not in days:
            print("Invalid entry. Please select from the options provided.")
        else:
            break

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
    city = city.lower()
    month = month.lower()
    day = day.lower()

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df.head()
    popular_month = df['month'].mode()[0]
    print('Most Popular Month: ', popular_month)

    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of the Week: ', popular_day)


    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', popular_end_station)


    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combi = df.start_end_station.mode().iloc[0]
    print('Most Popular Start and End Station Combination: ', popular_combi)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Time: " , df['Trip Duration'].sum())
    # display mean travel time
    print("Mean Travel Time: " , df['Trip Duration'].mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type Counts: " , df['User Type'].value_counts())

    if "Gender" in df.columns:
    # Display counts of gender
        print("Gender Counts: ", df['Gender'].value_counts())
    else:
        print("Gender does not exist in the dataset.")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("Most common Year of Birth: " , df['Birth Year'].mode()[0])
        print("Earliest Year of Birth: " , df['Birth Year'].min())
        print("Most Recent Year of Birth: " , df['Birth Year'].max())

    else:
        print("Year of Birth does not exist in the dataset.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def disp_data(df):
    index1 = 0
    index2 = 5

    while True:

        raw_data = input("Would you like to see 5 rows of data?\nPlease select yes or no.").lower()

        if raw_data == 'yes':

            print(df.iloc[index1:index2])

            index1 += 5

            index2 += 5

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
        disp_data(df)

        restart = input('\nWould you like to restart? Enter yes or no: \n')
        if restart.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
