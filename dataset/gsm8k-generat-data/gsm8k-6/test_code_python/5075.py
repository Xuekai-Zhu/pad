def solution():
    # Calculate the discount received and the total amount paid
    discount = (250 // 100) * 10  # for every $100 spent, $10 discount is given
    total_amount = 250 - discount
    
    result = total_amount
    return result

print(solution())