def solution():
    
    # Define the number of green jelly beans
    green_jelly_beans = 17

    # Define the number of red jelly beans
    red_jelly_beans = green_jelly_beans * 2

    # Calculate the total number of jelly beans
    total_jelly_beans = 60

    # Calculate the number of blue jelly beans
    blue_jelly_beans = total_jelly_beans - green_jelly_beans - red_jelly_beans

    # Display the number of blue jelly beans
    result = blue_jelly_beans
    return result

print(solution())