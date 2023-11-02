def solution():
    # Calculate the total number of books sold by the bookstore by Friday
    wednesday_sales = 15  # number of books sold on Wednesday
    thursday_sales = 3 * wednesday_sales  # number of books sold on Thursday, three times Wednesday's sales
    friday_sales = thursday_sales / 5  # number of books sold on Friday, one-fifth of Thursday's sales
    total_sales = wednesday_sales + thursday_sales + friday_sales  # total number of books sold
    result = total_sales
    return result

print(solution())