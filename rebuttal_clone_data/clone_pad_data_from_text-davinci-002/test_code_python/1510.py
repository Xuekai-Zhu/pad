def solution():
    team_size = 50
    percent_boys = 60
    percent_girls = 100 - percent_boys
    num_boys = team_size * (percent_boys / 100)
    num_girls = team_size - num_boys
    percent_junior_girls = 50
    num_junior_girls = num_girls * (percent_junior_girls / 100)
    result = num_junior_girls
    return result

print(solution())