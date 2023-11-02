def solution():
    # Calculate the total amount of money Cathy has now
    dad_amount = 25  # amount sent by dad
    mom_amount = 2 * dad_amount  # amount sent by mom, which is twice the amount sent by dad
    total_amount = 12 + dad_amount + mom_amount  # total amount of money Cathy has now
    result = total_amount
    return result

print(solution())