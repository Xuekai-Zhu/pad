def solution():
    
    original_price = 4
    new_price = 3
    num_dolls_saved_for = 15
    money_saved = original_price * num_dolls_saved_for
    num_dolls_discounted = money_saved // new_price
    result = num_dolls_discounted
    return result

print(solution())