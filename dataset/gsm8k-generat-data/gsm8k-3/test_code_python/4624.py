def solution():
    """Farmer Randy has 1700 acres of cotton he needs to have planted in 5 days.  With a crew of 2 tractors working for 2 days and then a crew of 7 tractors working for another 3 days, how many acres of cotton per day does each tractor need to plant to meet their planting deadline?"""
    # Define the total acres of cotton to be planted and the number of days allocated for planting
    total_acres = 1700
    total_days = 5

    # Define the number of tractors and days each crew will work
    crew1_tractors = 2
    crew1_days = 2
    crew2_tractors = 7
    crew2_days = 3

    # Calculate the total number of tractor hours
    total_tractor_hours = crew1_tractors * crew1_days + crew2_tractors * crew2_days

    # Calculate the daily planting rate per tractor
    planting_rate = total_acres / total_tractor_hours

    # Calculate the planting rate per tractor per day
    planting_rate_per_day = planting_rate / total_days

    # Display the planting rate per tractor per day
    result = planting_rate_per_day
    return result

print(solution())