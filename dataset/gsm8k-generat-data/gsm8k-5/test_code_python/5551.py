def solution():
    initial_amount = 450  # Delores starts with $450
    computer_cost = 400  # The computer costs $400
    printer_cost = 40  # The printer costs $40

    # Calculate the total cost of the computer and printer
    total_cost = computer_cost + printer_cost

    # Calculate how much money Delores has left
    remaining_money = initial_amount - total_cost
    result = remaining_money
    return result

print(solution())