def solution():
    num_rolls = 30
    tickets_per_roll = 100
    total_tickets = num_rolls * tickets_per_roll

    # Calculate the number of tickets bought by the 4th graders
    fourth_graders_tickets = int(total_tickets * 0.3)

    # Calculate the remaining number of tickets after the 4th graders bought some
    remaining_tickets = total_tickets - fourth_graders_tickets

    # Calculate the number of tickets bought by the 5th graders
    fifth_graders_tickets = int(remaining_tickets * 0.5)

    # Calculate the remaining number of tickets after the 5th graders bought some
    remaining_tickets -= fifth_graders_tickets

    # Calculate the number of tickets bought by the 6th graders
    sixth_graders_tickets = 100

    # Calculate the total number of tickets sold
    total_sold = fourth_graders_tickets + fifth_graders_tickets + sixth_graders_tickets

    # Calculate the number of tickets left unsold
    unsold_tickets = total_tickets - total_sold
    result = unsold_tickets
    return result

print(solution())