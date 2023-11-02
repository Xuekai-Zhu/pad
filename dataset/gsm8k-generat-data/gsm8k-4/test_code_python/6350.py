def solution():
    """Jackson's mother made little pizza rolls for Jackson's birthday party. Jackson ate 10 pizza rolls and his friend Jerome ate twice that amount. Tyler at one and half times more than Jerome. How many more pizza rolls did Tyler eat than Jackson?"""
    # Define the number of pizza rolls Jackson ate
    jackson_pizza_rolls = 10

    # Define the number of pizza rolls Jerome ate
    jerome_pizza_rolls = jackson_pizza_rolls * 2

    # Define the number of pizza rolls Tyler ate
    tyler_pizza_rolls = jerome_pizza_rolls * 1.5

    # Calculate the difference between Tyler and Jackson's pizza rolls
    pizza_roll_difference = tyler_pizza_rolls - jackson_pizza_rolls

    # return the result
    result = pizza_roll_difference
    return result

print(solution())