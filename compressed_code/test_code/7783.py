def solution():
    
    starting_data = 500
    youtube_data = 300
    remaining_data = starting_data - youtube_data
    facebook_data = (2/5) * remaining_data
    final_data = remaining_data - facebook_data
    result = final_data
    return result

print(solution())