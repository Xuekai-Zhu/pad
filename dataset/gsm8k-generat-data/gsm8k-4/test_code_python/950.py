def solution():
    """Theodore can craft 10 stone statues and 20 wooden statues every month. A stone statue costs $20 and a wooden statue costs $5. He also pays 10 percent of his total earnings in taxes. How much is his total earning every month?"""
    # Define the number of stone and wooden statues Theodore can craft
    stone_statues = 10
    wooden_statues = 20

    # Define the prices of stone and wooden statues
    stone_price = 20
    wooden_price = 5

    # Calculate the total earnings before taxes
    total_earnings = (stone_statues * stone_price) + (wooden_statues * wooden_price)

    # Calculate the amount of taxes
    taxes = total_earnings * 0.1

    # Calculate the net earnings
    net_earnings = total_earnings - taxes

    result = net_earnings
    return result

print(solution())