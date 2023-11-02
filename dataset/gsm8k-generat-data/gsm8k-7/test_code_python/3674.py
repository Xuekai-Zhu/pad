def solution():
    total_attendees = 120
    
    # Let's assume there are x female attendees
    # The number of male attendees is 4 more than x
    # So the total number of attendees is x + (x+4) = 2x + 4
    # We know that the total number of attendees is 120, so:
    2x + 4 = total_attendees
    
    # Solving for x, we get:
    x = (total_attendees - 4) / 2
    
    # The number of male attendees is x + 4
    num_male_attendees = x + 4
    result = num_male_attendees
    return result

print(solution())