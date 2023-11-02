def solution():
    milk_price = 1.5
    fruit_price = 2
    milk_needed = 10
    fruit_needed = 3
    num_batches = 3

    # Calculate the total cost of milk for three batches
    total_milk_cost = milk_price * milk_needed * num_batches

    # Calculate the total cost of fruit for three batches
    total_fruit_cost = fruit_price * fruit_needed * num_batches

    # Calculate the total cost of all ingredients for three batches
    total_cost = total_milk_cost + total_fruit_cost
    result = total_cost
    return result

print(solution())