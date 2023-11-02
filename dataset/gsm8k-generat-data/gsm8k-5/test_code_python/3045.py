def solution():
    rolls_of_tickets = 30  # The school ordered 30 rolls of tickets
    tickets_per_roll = 100  # Each roll of tickets has 100 tickets
    total_tickets = rolls_of_tickets * tickets_per_roll  # Total number of tickets available

    # Calculate the number of tickets bought by the 4th graders
    tickets_4th_graders = int(total_tickets * 0.3)

    # Calculate the number of tickets remaining after 4th graders bought their tickets
    tickets_remaining = total_tickets - tickets_4th_graders

    # Calculate the number of tickets bought by the 5th graders
    tickets_5th_graders = int(tickets_remaining * 0.5)

    # Calculate the number of tickets remaining after 5th graders bought their tickets
    tickets_remaining -= tickets_5th_graders

    # Calculate the number of tickets bought by the 6th graders
    tickets_6th_graders = 100

    # Calculate the number of tickets left unsold
    tickets_unsold = total_tickets - tickets_4th_graders - tickets_5th_graders - tickets_6th_graders
    result = tickets_unsold
    return result

print(solution())