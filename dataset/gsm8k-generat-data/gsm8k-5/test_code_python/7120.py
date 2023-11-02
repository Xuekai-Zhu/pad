def solution():
    deposit = 2000  # Adam's father deposited $2000 in the bank
    interest_rate = 0.08  # The bank offers 8% interest paid throughout the year
    years = 2.5  # Adam's father wants to know how much he will have after 2 and a half years

    # Calculate the total amount after 2 and a half years, including the deposit and interest received
    total_amount = deposit * (1 + interest_rate) ** years

    result = total_amount
    return result

print(solution())