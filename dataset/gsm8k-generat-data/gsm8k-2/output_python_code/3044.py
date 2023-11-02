def solution():
    """For the funfair, the school organizers ordered 30 rolls of tickets. Each roll of tickets has 100 tickets. The 4th graders bought 30% of the tickets while the 5th graders bought 50% of the remaining tickets. Then the 6th graders bought a total of 100 tickets. How many tickets were left unsold?"""
    rolls = 30
    tickets_per_roll = 100
    total_tickets = rolls * tickets_per_roll
    fourth_grade_tickets = int(total_tickets * 0.3)
    remaining_tickets = total_tickets - fourth_grade_tickets
    fifth_grade_tickets = int(remaining_tickets * 0.5)
    remaining_tickets -= fifth_grade_tickets
    sixth_grade_tickets = 100
    total_sold = fourth_grade_tickets + fifth_grade_tickets + sixth_grade_tickets
    unsold_tickets = total_tickets - total_sold
    result = unsold_tickets
    return result

print(solution())