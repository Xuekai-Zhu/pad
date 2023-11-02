def solution():
    """Lizzy had $30. She loaned out $15 to her friend. How much will Lizzy have if her friend returned the money with an interest of 20%?"""
    initial_amount = 30
    loaned_amount = 15
    returned_amount = loaned_amount * 1.2  # 20% interest
    total_amount = initial_amount + returned_amount
    result = total_amount
    
    return result

print(solution())