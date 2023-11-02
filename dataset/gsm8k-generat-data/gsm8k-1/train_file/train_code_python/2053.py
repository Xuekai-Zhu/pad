def solution():
    """A new book sold 15 copies at the bookstore on Wednesday. On Thursday the book sold three times that many copies. On Friday the book sold one-fifth the number of copies it did on Thursday. How many copies of the book did the bookstore sell by Friday?"""
    wednesday_sales = 15
    thursday_sales = 3 * wednesday_sales
    friday_sales = thursday_sales // 5
    total_sales = wednesday_sales + thursday_sales + friday_sales
    result = total_sales
    return result

print(solution())