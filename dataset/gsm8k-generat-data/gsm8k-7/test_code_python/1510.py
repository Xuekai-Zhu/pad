def solution():
    num_players = 50
    boys_percent = 60
    girls_percent = 100 - boys_percent
    girls_count = (girls_percent/100) * num_players
    
    # Divide girls_count by 2 to get half the girls and multiply by 0.5 to get number of junior girls
    num_junior_girls = (girls_count/2) * 0.5
    
    result = num_junior_girls
    return result

print(solution())