def solution():
    jack_black_height_inches = 66
    cdc_recommendation_inches = 72
    if jack_black_height_inches < cdc_recommendation_inches:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())