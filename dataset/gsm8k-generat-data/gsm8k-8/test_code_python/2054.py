def solution():
    # Calculate the number of copies sold on Thursday
    wednesday_sales = 15
    thursday_sales = 3 * wednesday_sales

    # Calculate the number of copies sold on Friday
    friday_sales = thursday_sales / 5

    # Calculate the total number of copies sold by Friday
    total_sales = wednesday_sales + thursday_sales + friday_sales
    result = total_sales
    return result

print(solution())