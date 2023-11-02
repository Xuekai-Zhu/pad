def solution():
    """John decides to fix a racecar. It cost $20,000 to fix but he gets a 20% discount. He wins his first race but only keeps 90% of the money. The prize is $70,000. How much money did he make from the car?"""
    # Define the initial cost of fixing the racecar and the discount he received
    initial_cost = 20000
    discount = 0.2

    # Calculate the final cost of fixing the racecar after the discount
    final_cost = initial_cost * (1 - discount)

    # Calculate the winnings from the race, after keeping only 90%
    winnings = 70000 * 0.9

    # Calculate the profit from the racecar
    profit = winnings - final_cost

    # return the result
    result = profit
    return result

print(solution())