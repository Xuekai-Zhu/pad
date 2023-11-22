def solution():
    
    # Define the initial amount of money Howard originally had
    initial_money = 100

    # Define the amount spent on Monday
    monday_spending = 8

    # Define the amount spent on Tuesday
    tuesday_spending = monday_spending * 2

    # Define the amount spent on Wednesday
    wednesday_spending = tuesday_spending * 4

    # Calculate the total amount spent
    total_spending = monday_spending + tuesday_spending + wednesday_spending

    # Calculate the amount of money Howard has left
    money_left = initial_money - total_spending

    # Display the amount of money Howard has left
    result = money_left
    return result

print(solution())