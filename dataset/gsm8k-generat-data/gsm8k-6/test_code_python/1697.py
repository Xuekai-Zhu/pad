def solution():
    # Calculate the amount of money left in the cookie jar
    initial_amount = 21
    doris_spent = 6
    martha_spent = doris_spent / 2
    money_left = initial_amount - doris_spent - martha_spent
    result = money_left
    return result

print(solution())