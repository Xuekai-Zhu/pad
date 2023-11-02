def solution():
    """Shelly has ten $10 bills and four fewer $5 bills. How much money does Shelly have in all?"""
    # Define the value of a $10 bill and a $5 bill
    ten_bill_value = 10
    five_bill_value = 5

    # Calculate the total value of the $10 bills
    total_ten_bills = ten_bill_value * 10

    # Calculate the total value of the $5 bills
    total_five_bills = (10 - 4) * five_bill_value

    # Calculate the total amount of money Shelly has
    total_money = total_ten_bills + total_five_bills

    # return the result
    result = total_money
    return result

print(solution())