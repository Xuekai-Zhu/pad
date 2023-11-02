def solution():
    """Randy has some money in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. If he had $104 dollars left in his piggy bank after a year, how much money, in dollars, did he have at first?"""
    # Define the number of trips to the store and the cost per trip
    TRIPS_PER_MONTH = 4
    COST_PER_TRIP = 2

    # Define the total number of months in a year
    MONTHS_PER_YEAR = 12

    # Calculate the total money spent on store trips in a year
    total_spent = TRIPS_PER_MONTH * COST_PER_TRIP * MONTHS_PER_YEAR

    # Calculate the money left in the piggy bank after a year
    final_amount = 104

    # Calculate the initial amount in the piggy bank
    initial_amount = final_amount + total_spent

    result = initial_amount
    return result

print(solution())