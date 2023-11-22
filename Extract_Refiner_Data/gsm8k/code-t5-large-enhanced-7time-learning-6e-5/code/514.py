def solution():
    
    # Define the initial amount of money
    initial_money = 4 * 10 + 6 * 20

    # Calculate the amount of money Ali gives to her sister
    sister_money = initial_money / 2

    # Calculate the remaining amount of money after buying dinner
    remaining_money = initial_money - sister_money
    dinner_money = remaining_money * (3/5)

    # Calculate the amount of money Ali has after buying dinner
    final_money = remaining_money - dinner_money

    # Display the amount of money Ali has after buying dinner
    result = final_money
    return result

print(solution())