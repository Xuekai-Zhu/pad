def solution():
    """For the funfair, the school organizers ordered 30 rolls of tickets. Each roll of tickets has 100 tickets. The 4th graders bought 30% of the tickets while the 5th graders bought 50% of the remaining tickets. Then the 6th graders bought a total of 100 tickets. How many tickets were left unsold?"""
    # Define the number of rolls of tickets and tickets per roll
    ROLLS_OF_TICKETS = 30
    TICKETS_PER_ROLL = 100

    # Calculate the total number of tickets
    total_tickets = ROLLS_OF_TICKETS * TICKETS_PER_ROLL

    # Calculate the number of tickets bought by 4th graders
    tickets_bought_4th = int(total_tickets * 0.3)

    # Subtract the tickets bought by 4th graders from the total tickets
    tickets_remaining_1 = total_tickets - tickets_bought_4th

    # Calculate the number of tickets bought by 5th graders
    tickets_bought_5th = int(tickets_remaining_1 * 0.5)

    # Subtract the tickets bought by 5th graders from the remaining tickets
    tickets_remaining_2 = tickets_remaining_1 - tickets_bought_5th

    # Calculate the number of tickets bought by 6th graders
    tickets_bought_6th = 100

    # Subtract the tickets bought by 6th graders from the remaining tickets
    unsold_tickets = tickets_remaining_2 - tickets_bought_6th

    # Display the number of unsold tickets
    result = unsold_tickets
    return result

print(solution())