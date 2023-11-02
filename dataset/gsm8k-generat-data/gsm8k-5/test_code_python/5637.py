def solution():
    tumbler_cost = 45  # Each tumbler costs $45
    num_tumblers = 10  # Mrs. Petersons bought 10 tumblers
    total_cost = tumbler_cost * num_tumblers  # Calculate the total cost of the tumblers
    amount_paid = 5 * 100  # Mrs. Petersons paid with five $100 bills
    change = amount_paid - total_cost  # Calculate the change Mrs. Petersons will receive
    result = change
    return result

print(solution())