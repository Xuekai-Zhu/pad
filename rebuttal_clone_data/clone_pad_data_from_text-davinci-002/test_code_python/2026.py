def solution():
    total_money = 150
    skate_cost = total_money / 2
    pad_cost = total_money - skate_cost - 25
    result = pad_cost
    return result
Question: 
At the library, Mona has read 26 books this year. She read 18 during the first 6 months of the year and 8 during the last 6 months. How many did she read per month, on average?

Solution:
def solution():
    total_books = 26
    books_read_first_half = 18
    books_read_second_half = 8
    average_books_read_per_month = total_books / 12
    result = average_books_read_per_month
    return result

print(solution())