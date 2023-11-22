def solution():
    
    # Define the number of jelly beans in the jar
    jelly_beans = 80

    # Calculate the number of jelly beans in the jar for each friend
    friend1 = jelly_beans / 2
    friend2 = friend1 + 20
    friend3 = friend1 * 1.25

    # Calculate the total number of jelly beans in the jar
    total_jelly_beans = jelly_beans + friend1 + friend2 + friend3

    # Calculate the average guess
    average_guess = total_jelly_beans / 3

    # Display the average guess
    result = average_guess
    return result

print(solution())