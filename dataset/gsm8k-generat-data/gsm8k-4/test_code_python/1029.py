def solution():
    """Farmer Red has three milk cows: Bess, Brownie, and Daisy. Bess, the smallest cow, gives him two pails of milk every day. Brownie, the largest cow, produces three times that amount. Then Daisy makes one pail more than Bess. How many pails of milk does Farmer Red get from them each week?"""
    # Define the amount of milk produced by each cow in pails per day
    bess_production = 2
    brownie_production = 3 * bess_production
    daisy_production = bess_production + 1

    # Calculate the total milk produced per day
    total_production = bess_production + brownie_production + daisy_production

    # Calculate the total milk produced per week
    total_weekly_production = total_production * 7

    # Return the result
    result = total_weekly_production
    return result

print(solution())