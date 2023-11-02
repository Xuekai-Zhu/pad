def solution():
    total_watermelons = 46
    one_melon_customers = 17
    three_melon_customers = 3
    # Calculate total number of watermelons bought by customers who bought one or three watermelons
    one_and_three_melon_total = (one_melon_customers * 1) + (three_melon_customers * 3)
    # Calculate the remaining number of watermelons sold to customers who bought two watermelons
    two_melon_total = total_watermelons - one_and_three_melon_total
    # Calculate the number of customers who bought two watermelons
    two_melon_customers = two_melon_total / 2
    result = two_melon_customers
    return result

print(solution())