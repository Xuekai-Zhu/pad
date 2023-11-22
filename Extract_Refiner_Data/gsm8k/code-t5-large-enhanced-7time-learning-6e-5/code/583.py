def solution():
    
    # Define the total number of jelly beans in the jar
    total_jelly_beans = 4500

    # Calculate the number of blue jelly beans in the jar
    blue_jelly_beans = total_jelly_beans / 0.01

    # Calculate the number of red jelly beans in the jar
    red_jelly_beans = blue_jelly_beans / 0.9

    # Calculate the number of green jelly beans in the jar
    green_jelly_beans = blue_jelly_beans * 1.1

    # Calculate the difference between the number of green and red jelly beans
    difference = green_jelly_beans - red_jelly_beans

    # Display the difference
    result = difference
    return result

print(solution())