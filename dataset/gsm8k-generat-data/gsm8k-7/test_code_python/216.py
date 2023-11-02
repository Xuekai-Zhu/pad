def solution():
    total_amount = 450
    last_year_amount = 0
    for i in range(1, 5):
        if i == 1:
            # Assume first year amount is x
            x = last_year_amount
            total_amount -= x
        else:
            # Calculate amount put in bank for current year
            current_year_amount = last_year_amount *2
            total_amount -= current_year_amount
            last_year_amount = current_year_amount
    
    result = x
    return result

print(solution())