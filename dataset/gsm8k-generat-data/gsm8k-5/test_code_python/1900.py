def solution():
    # Calculate the total number of yards Peyton threw on Saturday
    yards_at_50_degrees = 20  # when the temperature is 50 degrees Fahrenheit
    throws_on_saturday = 20  # Peyton threw the ball 20 times on Saturday
    total_yards_on_saturday = yards_at_50_degrees * throws_on_saturday

    # Calculate the total number of yards Peyton threw on Sunday
    yards_at_80_degrees = 2 * yards_at_50_degrees  # the ball moves twice as far at 80 degrees
    throws_on_sunday = 30  # Peyton threw the ball 30 times on Sunday
    total_yards_on_sunday = yards_at_80_degrees * throws_on_sunday
    
    # Calculate the total number of yards in the two days
    total_yards = total_yards_on_saturday + total_yards_on_sunday
    result = total_yards
    return result

print(solution())