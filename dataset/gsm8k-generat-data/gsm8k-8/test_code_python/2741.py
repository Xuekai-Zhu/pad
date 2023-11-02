def solution():
    # Define the cost of the trip and the amount of money Zoe already has
    trip_cost = 485
    grandma_money = 250

    # Calculate the amount of money Zoe needs to earn by selling candy bars
    candy_bar_money = trip_cost - grandma_money

    # Calculate the number of candy bars Zoe needs to sell
    candy_bars_needed = candy_bar_money / 1.25
    result = candy_bars_needed
    return result

print(solution())