def solution():
    # Define the variables
    remaining_money = 360
    magazine_spending = remaining_money / 4
    total_spending = remaining_money + magazine_spending
    grocery_spending = total_spending / 5

    # Calculate the initial amount of money
    initial_money = total_spending + grocery_spending
    result = initial_money
    return result

print(solution())