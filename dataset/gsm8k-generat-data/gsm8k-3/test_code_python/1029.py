def solution():
    """Farmer Red has three milk cows: Bess, Brownie, and Daisy. Bess, the smallest cow, gives him two pails of milk every day. Brownie, the largest cow, produces three times that amount. Then Daisy makes one pail more than Bess. How many pails of milk does Farmer Red get from them each week?"""
    # Calculate Bess's milk production
    bess_milk = 2 * 7 # 2 pails per day, 7 days per week

    # Calculate Brownie's milk production
    brownie_milk = 3 * bess_milk

    # Calculate Daisy's milk production
    daisy_milk = bess_milk + 1

    # Calculate the total milk production for the week
    total_milk = bess_milk + brownie_milk + daisy_milk

    # Display the total milk production
    result = total_milk
    return result

print(solution())