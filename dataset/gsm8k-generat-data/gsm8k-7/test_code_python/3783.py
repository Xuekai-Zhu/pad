def solution():
    num_students = 25
    num_chocolate = 10
    chocolate_price = 2
    num_glazed = 15
    glazed_price = 1

    # Calculate the total cost of all chocolate doughnuts
    total_chocolate_cost = num_chocolate * chocolate_price

    # Calculate the total cost of all glazed doughnuts
    total_glazed_cost = num_glazed * glazed_price

    # Calculate the total cost of all doughnuts
    total_cost = total_chocolate_cost + total_glazed_cost

    result = total_cost
    return result

print(solution())