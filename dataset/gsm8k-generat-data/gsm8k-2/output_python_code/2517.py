def solution():
    """Elsa gets 500 MB of cell phone data each month. If she spends 300 MB watching Youtube and 2/5 of what's left on Facebook, how many MB of data does she have left?"""
    total_data = 500
    youtube_data = 300
    remaining_data = total_data - youtube_data
    facebook_data = (2/5) * remaining_data
    data_left = remaining_data - facebook_data
    result = data_left
    return result

print(solution())