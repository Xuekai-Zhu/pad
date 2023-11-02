def solution():
    """Farmer Randy has 1700 acres of cotton he needs to have planted in 5 days. With a crew of 2 tractors working for 2 days and then a crew of 7 tractors working for another 3 days, how many acres of cotton per day does each tractor need to plant to meet their planting deadline?"""
    # Define the total number of acres of cotton to be planted and the number of days available
    total_acres = 1700
    total_days = 5

    # Define the number of tractors and the number of days each crew is working
    crew1_tractors = 2
    crew1_days = 2
    crew2_tractors = 7
    crew2_days = 3

    # Calculate the total number of tractor-days needed to plant the cotton
    total_tractor_days = (crew1_tractors * crew1_days) + (crew2_tractors * crew2_days)

    # Calculate the number of acres of cotton each tractor needs to plant per day to meet the planting deadline
    acres_per_day_per_tractor = total_acres / (total_tractor_days / total_days)

    # Round the result to 2 decimal places
    result = round(acres_per_day_per_tractor, 2)
    return result

print(solution())