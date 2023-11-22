def solution():
    
    # Define the initial amount of money Johnny had
    initial_money = 20

    # Define the amount of money Johnny added to his initial amount
    additional_money = 10

    # Calculate the total amount of money Johnny had after a year
    total_money = initial_money + additional_money

    # Calculate the amount of money Johnny invested in a year
    money_tripled = total_money * 3

    # Calculate the amount of money Johnny had after a year
    final_money = total_money - money_tripled

    # Display the final amount of money Johnny had after a year
    result = final_money
    return result

print(solution())