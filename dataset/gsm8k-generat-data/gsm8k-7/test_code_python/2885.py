def solution():
    june_savings = 27
    july_savings = 14
    august_savings = 21
    book_cost = 5
    shoe_cost = 17

    # Calculate the total amount saved
    total_saved = june_savings + july_savings + august_savings

    # Calculate the total amount spent
    total_spent = book_cost + shoe_cost

    # Calculate the amount of money left
    money_left = total_saved - total_spent
    result = money_left
    return result

print(solution())