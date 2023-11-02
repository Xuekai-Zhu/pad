def solution():
    """Wyatt's mother gave him $74 to go to the store. Wyatt bought 5 loaves of bread and 4 cartons of orange juice. Each loaf of bread cost $5 and each carton of orange juice cost $2. How much money does Wyatt have left?"""
    # Define the cost of each item
    bread_cost = 5
    juice_cost = 2

    # Calculate the total cost of the bread
    bread_total = bread_cost * 5

    # Calculate the total cost of the orange juice
    juice_total = juice_cost * 4

    # Calculate the total cost of the groceries
    total_cost = bread_total + juice_total

    # Calculate the amount of money Wyatt has left
    remaining_money = 74 - total_cost

    result = remaining_money
    return result

print(solution())