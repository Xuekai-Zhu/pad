def solution():
    # Calculate the total amount of money in the till
    total_money = 2*100 + 1*50 + 5*20 + 3*10 + 7*5 + 27*1

    # Calculate the amount of money Jack needs to leave in notes
    notes_to_leave = 300

    # Calculate the amount of money Jack needs to turn in to the main office
    money_to_turn_in = total_money - notes_to_leave

    result = money_to_turn_in
    return result

print(solution())