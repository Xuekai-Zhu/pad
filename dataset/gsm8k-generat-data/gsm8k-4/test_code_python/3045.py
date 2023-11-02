def solution():
    """For the funfair, the school organizers ordered 30 rolls of tickets. Each roll of tickets has 100 tickets. The 4th graders bought 30% of the tickets while the 5th graders bought 50% of the remaining tickets. Then the 6th graders bought a total of 100 tickets. How many tickets were left unsold?"""
    # Define the total number of rolls of tickets and the number of tickets per roll
    total_rolls = 30
    tickets_per_roll = 100

    # Calculate the total number of tickets ordered
    total_tickets = total_rolls * tickets_per_roll

    # Calculate the number of tickets bought by the 4th graders
    tickets_4th = total_tickets * 0.3

    # Calculate the number of tickets remaining after the 4th graders bought tickets
    remaining_tickets = total_tickets - tickets_4th

    # Calculate the number of tickets bought by the 5th graders
    tickets_5th = remaining_tickets * 0.5

    # Calculate the number of tickets remaining after the 5th graders bought tickets
    remaining_tickets -= tickets_5th

    # Calculate the number of tickets bought by the 6th graders
    tickets_6th = 100

    # Calculate the number of unsold tickets
    unsold_tickets = remaining_tickets - tickets_6th

    result = unsold_tickets
    return result

print(solution())