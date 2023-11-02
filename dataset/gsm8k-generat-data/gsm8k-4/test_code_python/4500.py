def solution():
    """Uncle Bradley has a $1000 bill that he wants to change into smaller bills so he could give them to his nieces and nephews. He wants to change 3/10 of the money into $50 bills while the rest into $100 bills. How many pieces of bills will Uncle Bradley have in all?"""
    
    # Define the total amount of money
    total_money = 1000
    
    # Calculate the amount of money to be changed into $50 bills
    money_in_fifties = total_money * 0.3
    
    # Calculate the number of $50 bills
    num_fifties = money_in_fifties / 50
    
    # Calculate the amount of money to be changed into $100 bills
    money_in_hundreds = total_money - money_in_fifties
    
    # Calculate the number of $100 bills
    num_hundreds = money_in_hundreds / 100
    
    # Calculate the total number of bills
    total_bills = num_fifties + num_hundreds
    
    # return the result
    result = total_bills
    return result

print(solution())