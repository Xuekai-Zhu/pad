def solution():
    
    # Define the initial amount of money and the cost of the trip
    initial_money = 50
    trip_cost = 300

    # Calculate the amount of money John has to cover
    cover_money = trip_cost / 2

    # Calculate the amount of money John is missing
    missing_money = initial_money - cover_money

    # Display the amount of money John is missing
    result = missing_money
    return result

print(solution())