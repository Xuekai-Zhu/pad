def solution():
    """Randy had $3,000. Smith gave him another $200. Randy then gave Sally $1,200 and kept the rest. What was the value, in dollars, of the rest?"""
    initial_amount = 3000
    additional_amount = 200
    amount_given = 1200
    
    total_amount = initial_amount + additional_amount
    remaining_amount = total_amount - amount_given
    
    result = remaining_amount
    return result

print(solution())