def solution():
    """Sid takes $48 with him on a shopping trip to the mall. He spent some of his money on computer accessories and another $8 on snacks. After these purchases, he only has $4 more than half of his original money left. How much did he spend on computer accessories?"""
    # Define the initial amount of money Sid has
    initial_money = 48

    # Define the amount of money Sid spent on snacks
    snacks_cost = 8

    # Define the remaining amount of money Sid has
    remaining_money = (initial_money - snacks_cost) / 2 + 4

    # Calculate the amount of money Sid spent on computer accessories
    computer_accessories_cost = initial_money - remaining_money - snacks_cost

    # return the result
    result = computer_accessories_cost
    return result

print(solution())