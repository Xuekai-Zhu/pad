def solution():
    cost_of_shoes = 120  # The cost of shoes Cary wants to buy
    saved_money = 30  # The amount of money Cary has already saved
    earnings_per_weekend = 5 * 3  # Cary earns $5 for every lawn he mows, and he mows 3 lawns each weekend

    # Calculate how much Cary still needs to save
    remaining_money = cost_of_shoes - saved_money

    # Calculate how many more weekends Cary will need to mow lawns to save up for the shoes
    weekends_needed = int((remaining_money / earnings_per_weekend) + 0.99)  # Add 0.99 to round up to the nearest weekend
    result = weekends_needed
    return result

print(solution())