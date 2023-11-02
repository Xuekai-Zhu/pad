def solution():
    """Olivia and Nigel are traveling in Asia.  Olivia has $112 and Nigel has $139. If together they buy six one day passes to a tourist attraction for $28 per ticket, how much money do they have left?"""
    # Define the initial amount of money Olivia and Nigel have
    olivia_money = 112
    nigel_money = 139

    # Calculate the cost of six one day passes to the tourist attraction
    ticket_cost = 28 * 6

    # Calculate the total amount of money Olivia and Nigel have left after buying the tickets
    total_money_left = olivia_money + nigel_money - ticket_cost

    # return the result
    result = total_money_left
    return result

print(solution())