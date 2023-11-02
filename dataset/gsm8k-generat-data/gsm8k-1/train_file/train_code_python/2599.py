def solution():
    """Emir wants to buy a dictionary that costs $5, a dinosaur book that costs $11, and a children's cookbook that costs $5. He has saved $19 from his allowance. How much more money does Emir need to buy all three books?"""
    dictionary_cost = 5
    dinosaur_book_cost = 11
    cookbook_cost = 5
    total_cost = dictionary_cost + dinosaur_book_cost + cookbook_cost
    saved_money = 19
    remaining_money = total_cost - saved_money
    result = remaining_money
    return result

print(solution())