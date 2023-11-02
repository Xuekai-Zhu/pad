def solution():
    """Bob started out the week with $80. On Monday alone, he spent half the money.
    On Tuesday, he spent one-fifth of the amount left from Monday. On Wednesday,
    he spent 3/8ths of the amount left from Tuesday. How much does he have left now?"""
    starting_amount = 80
    
    # Monday
    monday_spending = starting_amount / 2
    monday_remaining = starting_amount - monday_spending
    
    # Tuesday
    tuesday_spending = monday_remaining / 5
    tuesday_remaining = monday_remaining - tuesday_spending
    
    # Wednesday
    wednesday_spending = 3 * tuesday_remaining / 8
    wednesday_remaining = tuesday_remaining - wednesday_spending
    
    result = wednesday_remaining
    
    return result

print(solution())