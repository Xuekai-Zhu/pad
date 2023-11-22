def solution():
    
    # Define the dimensions of the jar
    jar_length = 6
    jar_width = 6
    jar_height = 15

    # Calculate the volume of the jar
    jar_volume = jar_length * jar_width * jar_height

    # Calculate the number of red jelly beans in the jar
    red_jelly_beans = jar_volume * 0.3

    # Calculate the distance off the guess
    distance_off = red_jelly_beans - 900

    # Display the distance off the guess
    result = distance_off
    return result

print(solution())