def solution():
    """Peyton Manning throws a football 20 yards when the temperature is 50 degrees Fahrenheit, but the ball moves twice as far when the temperature is 80 degrees Fahrenheit. Last Saturday, the temperature was 50 degrees Fahrenheit, and he threw the ball twenty times. On Sunday, the temperature rose to 80 degrees Fahrenheit, and he threw the ball 30 times. Calculate the total number of yards he threw the ball in the two days."""
    # Define the distance thrown at 50 degrees Fahrenheit and at 80 degrees Fahrenheit
    DISTANCE_50 = 20
    DISTANCE_80 = DISTANCE_50 * 2

    # Calculate the total distance thrown on Saturday
    saturday_distance = 20 * DISTANCE_50

    # Calculate the total distance thrown on Sunday
    sunday_distance = 30 * DISTANCE_80

    # Calculate the total distance thrown over the two days
    total_distance = saturday_distance + sunday_distance

    # Display the total distance thrown
    result = total_distance
    return result

print(solution())