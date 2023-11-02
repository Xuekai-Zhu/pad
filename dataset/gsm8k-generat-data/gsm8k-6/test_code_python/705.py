def solution():
    # Let x be the initial amount of money Isabel had
    # After buying the toy, she had x/2 dollars left
    # After buying the book, she had (x/2)/2 = x/4 dollars left
    # If she has 51 dollars left after these purchases, then she spent (x/2) + (x/4) = 3x/4 dollars
    # The amount of money she had at first was x = 4/3 * (total amount of money spent)
    
    total_spent = (4/3) * 51  # total amount of money Isabel spent
    initial_money = round(total_spent, 2)  # rounding to 2 decimal places
    result = initial_money
    return result

print(solution())