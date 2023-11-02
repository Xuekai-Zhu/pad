def solution():
    sandwich_cost = 4  # Sandwich cost is $4
    juice_cost = 2 * sandwich_cost  # Juice cost is twice the sandwich cost
    milk_cost = 0.75 * (sandwich_cost + juice_cost)  # Milk cost is 75% of the total cost of sandwich and juice
    total_cost = sandwich_cost + juice_cost + milk_cost  # Total cost of food

    result = total_cost
    return result

print(solution())