def solution():
    """James writes a comic every other day for 4 years. If there was no leap year, how many comics has he written?"""
    # Define the number of years James writes comics for
    years = 4

    # Define the number of days in a non-leap year
    days_in_year = 365

    # Calculate the total number of days James writes comics for
    total_days = years * days_in_year

    # Calculate the number of comics James writes (assuming he writes every other day)
    comics = total_days // 2

    # Display the number of comics James has written
    result = comics
    return result

print(solution())