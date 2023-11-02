def solution():
    """Emir wants to buy a dictionary that costs $5, a dinosaur book that costs $11, and a children's cookbook that costs $5. He has saved $19 from his allowance. How much more money does Emir need to buy all three books?"""
    dictionary_cost = 5
    book_cost = 11
    cookbook_cost = 5
    total_cost = dictionary_cost + book_cost + cookbook_cost
    savings = 19
    remaining_cost = total_cost - savings
    result = remaining_cost
    return result

print(solution())