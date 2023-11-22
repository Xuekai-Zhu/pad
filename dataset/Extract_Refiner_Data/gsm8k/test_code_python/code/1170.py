def solution():
    
    # Define the initial amount of money and the number of dollar bills
    initial_money = 1000
    num_bills = 20

    # Calculate the remaining money after losing 10 bills
    remaining_money = initial_money - 10 * num_bills

    # Calculate the number of dollar bills that can be paid for each bill
    num_paid_bills = remaining_money / 2

    # Calculate the total number of dollar bills
    total_bills = remaining_money * num_bills

    # Calculate the number of 5 dollar bills
    num_bills_5 = total_bills // 5

    # Display the number of 5 dollar bills
    result = num_bills_5
    return result

print(solution())