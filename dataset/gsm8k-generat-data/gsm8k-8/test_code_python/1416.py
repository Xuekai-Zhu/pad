def solution():
    # Define the typing speeds of each employee
    rudy_speed = 64
    joyce_speed = 76
    gladys_speed = 91
    lisa_speed = 80
    mike_speed = 89

    # Calculate the total typing speed of the team
    total_speed = rudy_speed + joyce_speed + gladys_speed + lisa_speed + mike_speed

    # Calculate the average typing speed of the team
    average_speed = total_speed / 5
    result = average_speed
    return result

print(solution())