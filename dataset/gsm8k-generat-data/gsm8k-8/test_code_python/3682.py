def solution():
    total_money = 100
    five_bills = 4
    twenty_bills = 3
    # Calculate the total amount of money from the $5 and $20 bills
    total_fives_and_twenty = (5 * five_bills) + (20 * twenty_bills)
    # Calculate the amount of money from the $10 bills
    total_tens = total_money - total_fives_and_twenty
    # Calculate the number of $10 bills
    num_tens = total_tens / 10
    result = num_tens
    return result

print(solution())