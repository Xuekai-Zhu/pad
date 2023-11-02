def solution():
    # Define the total amount of money Uncle Bradley has
    total_money = 1000

    # Calculate the amount of money he wants to change into $50 bills
    fifty_bill_money = 3/10 * total_money

    # Calculate the number of $50 bills he will have
    num_fifty_bills = fifty_bill_money / 50

    # Calculate the amount of money he wants to change into $100 bills
    hundred_bill_money = total_money - fifty_bill_money

    # Calculate the number of $100 bills he will have
    num_hundred_bills = hundred_bill_money / 100

    # Calculate the total number of bills he will have
    total_bills = num_fifty_bills + num_hundred_bills

    result = total_bills
    return result

print(solution())