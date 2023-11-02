def solution():
    """Jesse received $50 as a gift to buy what she wants. She goes to the mall and falls in love with a novel that costs her $7. Then she went to lunch because she was very hungry and spent twice as much as the novel cost her. How much money did Jesse have left after going to the mall?"""
    # Define the initial amount of money Jesse received as a gift
    initial_amount = 50

    # Define the cost of the novel
    novel_cost = 7

    # Calculate the cost of lunch
    lunch_cost = novel_cost * 2

    # Calculate the total amount spent at the mall
    total_cost = novel_cost + lunch_cost

    # Calculate the amount of money Jesse has left
    amount_left = initial_amount - total_cost

    result = amount_left
    return result

print(solution())