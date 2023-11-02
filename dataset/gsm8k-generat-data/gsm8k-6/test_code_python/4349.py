def solution():
    # Convert all times to minutes
    mars_time = 1210
    jupiter_time = mars_time + 2*60 + 41
    uranus_time = jupiter_time + 3*60 + 16

    # Calculate the minutes from 6:00 AM until Uranus first appears
    total_minutes = uranus_time - (6*60)
    result = total_minutes
    return result

print(solution())