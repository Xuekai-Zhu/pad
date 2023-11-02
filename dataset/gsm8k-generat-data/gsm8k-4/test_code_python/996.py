def solution():
    """A club opens up and charges $20 to enter. James buys 2 rounds for his 5 friends. He also buys 6 drinks for himself. Drinks cost $6 each. He decides to eat some food so he orders some fried chicken which costs $14. He leaves a 30% tip on everything he orders. How much did he spend for the night?"""
    # Define the cost of entry to the club
    club_entry = 20

    # Define the cost of drinks
    drink_cost = 6

    # Calculate the cost of James' drinks
    james_drinks = 6 * 6

    # Calculate the cost of the rounds of drinks for James' friends
    friend_drinks = 2 * drink_cost * 5

    # Calculate the cost of James' food
    james_food = 14

    # Calculate the total cost before tip
    total_cost = club_entry + james_drinks + friend_drinks + james_food

    # Calculate the tip amount
    tip_amount = total_cost * 0.3

    # Calculate the total cost including tip
    total_cost_with_tip = total_cost + tip_amount

    # Return the result
    result = total_cost_with_tip
    return result

print(solution())