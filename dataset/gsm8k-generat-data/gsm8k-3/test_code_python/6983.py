def solution():
    """A Ferris wheel can accommodate 70 people in 20 minutes.  If the Ferris wheel is open from 1:00 pm until 7:00 pm, how many people will get to ride?"""
    # Define the number of minutes the Ferris wheel is in operation
    MINUTES_IN_OPERATION = 6 * 60

    # Define the number of people the Ferris wheel can accommodate in 1 minute
    PEOPLE_PER_MINUTE = 70 / 20

    # Calculate the total number of people who can ride the Ferris wheel in the given timeframe
    total_people = MINUTES_IN_OPERATION * PEOPLE_PER_MINUTE

    # Display the total number of people who can ride
    result = total_people
    return result

print(solution())