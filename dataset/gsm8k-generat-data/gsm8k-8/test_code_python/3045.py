def solution():
    # Calculate the total number of tickets
    total_tickets = 30 * 100

    # Calculate the number of tickets bought by the 4th graders
    fourth_graders_tickets = total_tickets * 0.3

    # Calculate the number of tickets remaining
    remaining_tickets = total_tickets - fourth_graders_tickets

    # Calculate the number of tickets bought by the 5th graders
    fifth_graders_tickets = remaining_tickets * 0.5

    # Calculate the number of tickets remaining
    remaining_tickets = remaining_tickets - fifth_graders_tickets

    # Calculate the number of tickets bought by the 6th graders
    sixth_graders_tickets = 100

    # Calculate the number of tickets left unsold
    unsold_tickets = total_tickets - fourth_graders_tickets - fifth_graders_tickets - sixth_graders_tickets

    result = unsold_tickets
    return result

print(solution())