def solution():
    data_limit = 500
    youtube_data = 300
    remaining_data = data_limit - youtube_data
    facebook_data = (2/5) * remaining_data
    data_left = remaining_data - facebook_data
    result = data_left
    return result

print(solution())