def solution():
    """Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?"""
    # Define the number of pills and the prices
    pills_per_day = 9
    expensive_price = 1.5 + 5.5
    cheap_price = 1.5

    # Calculate the total cost of the expensive pills
    expensive_pills_per_day = pills_per_day - 4
    expensive_pills_cost = expensive_pills_per_day * expensive_price
    expensive_pills_total_cost = expensive_pills_cost * 14

    # Calculate the total cost of the cheap pills
    cheap_pills_per_day = 4
    cheap_pills_cost = cheap_pills_per_day * cheap_price
    cheap_pills_total_cost = cheap_pills_cost * 14

    # Calculate the total cost of all the pills
    total_cost = expensive_pills_total_cost + cheap_pills_total_cost

    # Return the result
    result = total_cost
    return result

print(solution())