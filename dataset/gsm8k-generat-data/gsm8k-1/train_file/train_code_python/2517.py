def solution():
    """Elsa gets 500 MB of cell phone data each month. If she spends 300 MB watching Youtube and 2/5 of what's left on Facebook, how many MB of data does she have left?"""
    starting_data = 500
    youtube_data = 300
    remaining_data = starting_data - youtube_data
    facebook_data = (2/5) * remaining_data
    final_data = remaining_data - facebook_data
    result = final_data
    return result

print(solution())