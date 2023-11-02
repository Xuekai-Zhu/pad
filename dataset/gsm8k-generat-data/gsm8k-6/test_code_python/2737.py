def solution():
    # Calculate the total number of children and adults visiting the zoo on Monday and Tuesday
    total_children = 7 + 4
    total_adults = 5 + 2
    
    # Calculate the total amount of money made for child and adult tickets on Monday and Tuesday
    total_money_earned = (total_children * 3) + (total_adults * 4)

    result = total_money_earned
    return result

print(solution())