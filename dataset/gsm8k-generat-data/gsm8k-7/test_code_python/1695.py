def solution():
    num_games = 20
    attendance_rate = 0.9

    # Calculate the number of games Tara's dad attended in the first year
    num_attended_first_year = num_games * attendance_rate

    # Calculate the number of games Tara's dad attended in the second year
    num_attended_second_year = num_attended_first_year - 4
    
    result = num_attended_second_year
    return result

print(solution())