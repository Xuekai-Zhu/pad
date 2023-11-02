def solution():
    # Calculate the number of words Bo already knew
    words_knew = 0.2 * 800  

    # Calculate the number of words Bo needs to learn
    words_left = 800 - words_knew  

    # Calculate the number of words Bo needs to learn per day
    words_per_day = words_left / 40  
    result = words_per_day
    return result

print(solution())