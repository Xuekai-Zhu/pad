def solution():
    first_ticket_cost = 150
    second_ticket_cost = 150
    third_ticket_cost = first_ticket_cost / 3
    roommate_share = 0.5

    # Calculate the total cost of all three parking tickets
    total_cost = (first_ticket_cost + second_ticket_cost + third_ticket_cost)

    # Calculate the amount paid by the roommate
    roommate_contribution = roommate_share * total_cost

    # Calculate the remaining cost to be paid by James
    james_cost = total_cost - roommate_contribution

    # Calculate how much money James has left in the bank
    bank_balance = 500
    money_left = bank_balance - james_cost
    result = money_left
    return result

print(solution())