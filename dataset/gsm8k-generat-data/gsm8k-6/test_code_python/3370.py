def solution():
    # Calculate the number of customers who bought two watermelons
    customers = 46 - 17 - 3*3  # seventeen customers bought one melon, three customers bought three melons
    two_melons_customers = customers // 2  # divide by 2 since each customer bought two melons
    result = two_melons_customers
    return result

print(solution())