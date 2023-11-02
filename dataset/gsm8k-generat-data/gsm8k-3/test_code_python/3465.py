def solution():
    """Wyatt's mother gave him $74 to go to the store. Wyatt bought 5 loaves of bread and 4 cartons of orange juice. 
       Each loaf of bread cost $5 and each carton of orange juice cost $2. How much money does Wyatt have left?"""
    # Define the cost of bread and orange juice
    BREAD_COST = 5
    ORANGE_JUICE_COST = 2

    # Define the number of loaves of bread and cartons of orange juice purchased
    bread_count = 5
    orange_juice_count = 4

    # Calculate the total cost of the bread and orange juice
    total_cost = (bread_count * BREAD_COST) + (orange_juice_count * ORANGE_JUICE_COST)

    # Calculate and display the money Wyatt has left
    money_left = 74 - total_cost
    result = money_left
    return result

print(solution())