def solution():
    
    total_fights = 190
    knockout_percentage = 0.5
    first_round_percentage = 0.2
    total_knockouts = total_fights * knockout_percentage
    first_round_knockouts = total_knockouts * first_round_percentage
    result = first_round_knockouts
    return result

print(solution())