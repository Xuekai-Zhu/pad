def solution():
    
    # Define the number of laps Bethany can run
    bethany_laps = 10

    # Define the number of laps Trey can run
    trey_laps = bethany_laps + 4

    # Define the number of laps Shaelyn can run
    shaelyn_laps = trey_laps / 2

    # Define the number of laps Quinn can run
    quinn_laps = shaelyn_laps - 2

    # Calculate the difference in the number of laps Bethany and Quinn can run
    diff_laps = bethany_laps - quinn_laps

    # Display the difference in the number of laps Bethany and Quinn can run
    result = diff_laps
    return result

print(solution())