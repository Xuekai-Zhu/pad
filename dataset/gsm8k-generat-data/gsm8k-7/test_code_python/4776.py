def solution():
    current_year_attendees = 600
    next_year_attendees = current_year_attendees * 2
    last_year_attendees = next_year_attendees - 200

    # Calculate the total number of people at the fair in the next 3 years
    total_attendees = current_year_attendees + next_year_attendees + last_year_attendees
    result = total_attendees
    return result

print(solution())