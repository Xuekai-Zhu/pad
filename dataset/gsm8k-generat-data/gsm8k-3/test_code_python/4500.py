def solution():
    """Uncle Bradley has a $1000 bill that he wants to change into smaller bills so he could give them to his nieces and nephews. He wants to change 3/10 of the money into $50 bills while the rest into $100 bills. How many pieces of bills will Uncle Bradley have in all?"""
    # Define the total amount of money Uncle Bradley has
    total_money = 1000

    # Calculate the amount of money that Uncle Bradley wants to change into $50 bills
    fifty_bill_money = total_money * (3/10)

    # Calculate the number of $50 bills that Uncle Bradley will have
    num_fifty_bills = fifty_bill_money / 50

    # Calculate the amount of money that Uncle Bradley wants to change into $100 bills
    hundred_bill_money = total_money - fifty_bill_money

    # Calculate the number of $100 bills that Uncle Bradley will have
    num_hundred_bills = hundred_bill_money / 100

    # Calculate the total number of bills that Uncle Bradley will have
    total_bills = num_fifty_bills + num_hundred_bills

    # Display the total number of bills
    result = total_bills
    return result

print(solution())