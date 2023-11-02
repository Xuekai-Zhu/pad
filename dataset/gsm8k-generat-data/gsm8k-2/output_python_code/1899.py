def solution():
    """Peyton Manning throws a football 20 yards when the temperature is 50 degrees Fahrenheit, but the ball moves twice as far when the temperature is 80 degrees Fahrenheit. Last Saturday, the temperature was 50 degrees Fahrenheit, and he threw the ball twenty times. On Sunday, the temperature rose to 80 degrees Fahrenheit, and he threw the ball 30 times. Calculate the total number of yards he threw the ball in the two days."""
    temp_50_yards = 20
    temp_80_yards = 2 * temp_50_yards
    saturday_throws = 20
    sunday_throws = 30
    saturday_yards = saturday_throws * temp_50_yards
    sunday_yards = sunday_throws * temp_80_yards
    total_yards = saturday_yards + sunday_yards
    result = total_yards
    return result

print(solution())