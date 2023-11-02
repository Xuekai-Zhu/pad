def solution():
    # Calculate the number of crickets eaten on the first day
    crickets_first_day = round(0.3 * 70)  

    # Calculate the number of crickets eaten on the second day
    crickets_second_day = crickets_first_day - 6  

    # Calculate the number of crickets eaten on the third day
    crickets_third_day = 70 - crickets_first_day - crickets_second_day  

    result = crickets_third_day
    return result

print(solution())