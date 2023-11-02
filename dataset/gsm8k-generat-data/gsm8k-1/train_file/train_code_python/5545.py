def solution():
    """Shelly has ten $10 bills and four fewer $5 bills. How much money does Shelly have in all?"""
    num_ten_bills = 10
    num_five_bills = num_ten_bills - 4
    ten_bill_value = 10
    five_bill_value = 5
    total_value = (num_ten_bills * ten_bill_value) + (num_five_bills * five_bill_value)
    result = total_value
    return result

print(solution())