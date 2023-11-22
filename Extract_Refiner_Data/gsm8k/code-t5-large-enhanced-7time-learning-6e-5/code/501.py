def solution():
    
    # Define the number of sticks that can be made from a 2 x 4 piece of wood
    sticks_4 = 200

    # Define the number of sticks that can be made from a 2 x 8 piece of wood
    sticks_8 = 400

    # Define the cost of a 2 x 4 piece of wood and a 2 x 8 piece of wood
    cost_4 = 4
    cost_8 = 6

    # Define the amount of money Frederick has to spend on wood for sticks
    money_4 = 24

    # Calculate the total number of sticks that can be made
    total_sticks = (sticks_4 * cost_4) + (sticks_8 * cost_8)

    # Determine the cheaper lumber of wood
    if money_4 < money_8:
        cheaper_lumber = "lumber"
        sticks_4 = 200
        sticks_8 = 400
    else:
        cheaper_lumber = "lumber"

    # Calculate the total cost of

print(solution())