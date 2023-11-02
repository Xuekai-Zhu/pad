def solution():
    """Peyton Manning throws a football 20 yards when the temperature is 50 degrees Fahrenheit, but the ball moves twice as far
    when the temperature is 80 degrees Fahrenheit. Last Saturday, the temperature was 50 degrees Fahrenheit, and he threw the
    ball twenty times. On Sunday, the temperature rose to 80 degrees Fahrenheit, and he threw the ball 30 times. Calculate the
    total number of yards he threw the ball in the two days."""
    yards_at_50 = 20
    yards_at_80 = yards_at_50 * 2
    temp_saturday = 50
    temp_sunday = 80
    throws_saturday = 20
    throws_sunday = 30
    total_yards_saturday = yards_at_50 * throws_saturday
    total_yards_sunday = yards_at_80 * throws_sunday
    total_yards = total_yards_saturday + total_yards_sunday
    result = total_yards
    return result

print(solution())