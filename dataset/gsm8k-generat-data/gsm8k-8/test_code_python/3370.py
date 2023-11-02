def solution():
    # Calculate the total number of watermelons sold
    total_melons = 46

    # Calculate the number of customers that bought one watermelon
    one_melon_customers = 17

    # Calculate the number of melons bought by customers that bought three melons
    three_melon_customers = 3
    three_melon_total = 3 * three_melon_customers

    # Calculate the total number of melons bought by customers that bought two melons
    two_melon_total = total_melons - one_melon_customers - three_melon_total

    # Calculate the number of customers that bought two watermelons
    two_melon_customers = two_melon_total / 2

    result = two_melon_customers
    return result

print(solution())