def solution():
    # Calculate the total words typed by each team member in one minute
    rudy_speed = 64
    joyce_speed = 76
    gladys_speed = 91
    lisa_speed = 80
    mike_speed = 89

    # Calculate the average speed of the team
    team_speed = (rudy_speed + joyce_speed + gladys_speed + lisa_speed + mike_speed) / 5

    result = team_speed
    return result

print(solution())