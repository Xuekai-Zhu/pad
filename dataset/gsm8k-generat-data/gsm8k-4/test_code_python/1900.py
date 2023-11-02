def solution():
    """Peyton Manning throws a football 20 yards when the temperature is 50 degrees Fahrenheit, but the ball moves twice as far when the temperature is 80 degrees Fahrenheit. Last Saturday, the temperature was 50 degrees Fahrenheit, and he threw the ball twenty times. On Sunday, the temperature rose to 80 degrees Fahrenheit, and he threw the ball 30 times. Calculate the total number of yards he threw the ball in the two days."""
    # Define the distance thrown at 50 degrees Fahrenheit and 80 degrees Fahrenheit
    distance_50 = 20
    distance_80 = distance_50 * 2

    # Calculate the total distance thrown on Saturday and Sunday
    total_distance = (distance_50 * 20) + (distance_80 * 30)

    result = total_distance
    return result

print(solution())