def solution():
    # Calculate the number of free triple cheese pizzas and total cost of triple cheese pizzas
    free_triple_cheese = 10 // 2
    total_cost_triple_cheese = (10 - free_triple_cheese) * 5

    # Calculate the number of free meat lovers pizzas and total cost of meat lovers pizzas
    free_meat_lovers = 9 // 3
    total_cost_meat_lovers = (9 - free_meat_lovers) * 5 * 2

    # Calculate the total cost of all pizzas
    total_cost = total_cost_triple_cheese + total_cost_meat_lovers

    result = total_cost
    return result

print(solution())