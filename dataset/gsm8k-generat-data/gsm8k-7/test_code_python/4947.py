def solution():
    num_tickets = 3
    num_winning_numbers = 5
    value_per_winning_number = 20

    # Calculate the total number of winning numbers across all tickets
    total_winning_numbers = num_tickets * num_winning_numbers

    # Calculate the total value of all winning numbers
    total_winning_value = total_winning_numbers * value_per_winning_number
    result = total_winning_value
    return result

print(solution())