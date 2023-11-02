def solution():
    # Calculate the number of handball trophies Jack will have in three years
    jack_trophies = 10 * (30 + 100)  # Michael has 30 trophies now, and his number of trophies will increase by 100 in three years
                                     # Jack will have ten times more than the number of Michael's trophies in three years
    total_trophies = jack_trophies + 30 + 100  # Total number of trophies after three years
    result = total_trophies
    return result

print(solution())