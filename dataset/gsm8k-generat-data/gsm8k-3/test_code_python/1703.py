def solution():
    """School coaches bought sports equipment. Coach A bought ten new basketballs for $29 each, while coach B bought 14 new baseballs for $2.50 each and a baseball bat for $18. How much more did coach A spend than coach B?"""
    # Define the number of items and their prices for each coach
    A_basketballs = 10
    A_price = 29
    B_baseballs = 14
    B_baseball_price = 2.5
    B_bat_price = 18

    # Calculate the total cost for each coach
    A_cost = A_basketballs * A_price
    B_cost = (B_baseballs * B_baseball_price) + B_bat_price

    # Calculate the difference in cost
    difference = A_cost - B_cost

    # Display the difference in cost
    result = difference
    return result

print(solution())