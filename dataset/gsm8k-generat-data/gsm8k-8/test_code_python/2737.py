def solution():
    # Calculate the total number of children and adults that went to the zoo
    total_children = 7 + 4
    total_adults = 5 + 2

    # Calculate the total amount of money made on Monday
    monday_sales = (total_children * 3) + (total_adults * 4)

    # Calculate the total amount of money made on Tuesday
    tuesday_sales = (4 * 3) + (2 * 4)

    # Calculate the total amount of money made for both days
    total_sales = monday_sales + tuesday_sales
    result = total_sales
    return result

print(solution())