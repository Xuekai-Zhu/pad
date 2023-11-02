def solution():
    total_attendees = 120  # There are 120 conference attendees
    # Let x be the number of female attendees, then there are x + 4 male attendees
    # Therefore, we can write the equation:
    # x + (x + 4) = 120
    # Solving for x gives x = 58, which is the number of female attendees
    male_attendees = 58 + 4  # There are 4 more male attendees than female attendees
    result = male_attendees
    return result

print(solution())