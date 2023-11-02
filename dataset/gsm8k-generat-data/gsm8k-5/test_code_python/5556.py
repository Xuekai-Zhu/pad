def solution():
    computer_cost = 400  # The cost of the computer is $400
    printer_cost = 40  # The cost of the printer is $40
    remaining_money = 10  # Delores has $10 left after buying the computer and the printer

    # Calculate the total cost of the computer and the printer
    total_cost = computer_cost + printer_cost

    # Calculate how much money Delores had at first
    initial_money = total_cost + remaining_money
    result = initial_money
    return result

print(solution())