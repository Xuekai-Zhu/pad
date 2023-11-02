def solution():
    # Calculate the number of books sold on Tuesday and Wednesday
    tuesday_sales = 7
    wednesday_sales = 3 * tuesday_sales

    # Calculate the sales from Wednesday tripled
    wednesday_tripled = 3 * wednesday_sales

    # Calculate the total number of books sold
    total_sales = tuesday_sales + wednesday_sales + wednesday_tripled

    result = total_sales
    return result

print(solution())