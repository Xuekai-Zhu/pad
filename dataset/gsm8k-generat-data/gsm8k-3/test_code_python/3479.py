def solution():
    """Pat is hunting for sharks to take photos. For every photo he takes he earns $15. He sees a shark about every 10 minutes. His boat fuel costs $50 an hour. If he shark hunts for 5 hours, how much money can he expect to make in profit?"""
    # Define the rate at which Pat sees sharks
    shark_rate = 6  # 6 sharks per hour

    # Calculate the total number of sharks Pat is likely to see
    total_sharks = shark_rate * 5  # 30 Sharks

    # Calculate the total amount of money Pat can earn from taking photos
    photo_earnings = total_sharks * 15  # $450

    # Calculate the total cost of fuel for the 5 hours
    fuel_cost = 50 * 5  # $250

    # Calculate the total profit
    total_profit = photo_earnings - fuel_cost

    # Display the total profit
    result = total_profit
    return result

print(solution())