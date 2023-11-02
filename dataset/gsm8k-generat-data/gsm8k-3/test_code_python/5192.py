def solution():
    """Martha gets prize points every time she shops at her local grocery store. She gets 50 points per $10 spent, plus a 250 point bonus if she spends more than $100. Martha buys 3 pounds of beef for $11 each, 8 pounds of fruits and vegetables for $4/pound, 3 jars of spices for $6 each, and other groceries totaling $37. How many points does Martha get?"""
    # Define the price of each item
    BEEF_PRICE = 11
    FRUIT_PRICE = 4
    SPICE_PRICE = 6

    # Define the amount of each item purchased
    beef_pounds = 3
    fruit_pounds = 8
    spice_jars = 3
    other_total = 37

    # Calculate the total cost of each type of item
    beef_cost = beef_pounds * BEEF_PRICE
    fruit_cost = fruit_pounds * FRUIT_PRICE
    spice_cost = spice_jars * SPICE_PRICE
    total_cost = beef_cost + fruit_cost + spice_cost + other_total

    # Calculate the bonus points if Martha spends more than $100
    if total_cost > 100:
        bonus_points = 250
    else:
        bonus_points = 0

    # Calculate the total prize points Martha will get
    prize_points = (total_cost // 10) * 50 + bonus_points

    # Display the total prize points
    result = prize_points
    return result

print(solution())