def solution():
    initial_number_of_balloons = 50
    balloons_lost = 12
    balloons_given_away = 9
    balloons_grabbed = 11
    total_number_of_balloons = initial_number_of_balloons - balloons_lost + balloons_given_away + balloons_grabbed
    result = total_number_of_balloons
    
    return result

print(solution())