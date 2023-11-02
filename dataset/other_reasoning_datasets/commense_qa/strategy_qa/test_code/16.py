def solution():
    spirit_final_transmission_year = 2010
    another_rover_final_words_year = 2019
    current_year = 2020
    if spirit_final_transmission_year == current_year:
        result = "yes"
    elif another_rover_final_words_year == current_year:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())