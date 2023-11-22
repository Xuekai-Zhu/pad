def solution():
    
    # Define the initial capital amount
    initial_capital = 5000

    # Calculate the total amount of money from the two banks
    bank1_money = 4000
    bank2_money = bank1_money * 2
    total_money = bank1_money + bank2_money

    # Calculate the new capital amount
    new_capital = initial_capital + total_money

    # return the result
    result = new_capital
    return result

print(solution())