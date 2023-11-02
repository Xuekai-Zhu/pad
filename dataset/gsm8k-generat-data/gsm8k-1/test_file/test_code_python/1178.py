def solution():
    """Bob spends $27000 distributed between 3 schools to buy books. He can buy 100 books for $500. How many books can he buy per school?"""
    total_budget = 27000
    schools = 3
    cost_per_book = 500
    books_per_school = (total_budget / schools) / cost_per_book
    result = books_per_school
    return result

print(solution())