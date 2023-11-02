def solution():
    
    # Define the initial amount of money Thomas withdraws and the number of bills he loses
    initial_money = 1000
    lost_bills = 10

    # Calculate the remaining amount of money after losing 10 bills
    remaining_money = initial_money - lost_bills

    # Calculate the number of bills used to pay for a bill
    used_bills = remaining_money / 2

    # Calculate the remaining amount of money after using half of the remaining bills
    remaining_money -= used_bills

    # Calculate the number of 5 dollar bills Thomas can convert his money to 5 dollar bills
    five_dollar_bills = remaining_money / 5

    # Display the number of 5 dollar bills Thomas has
    result = five_dollar_bills
    return result

print(solution())