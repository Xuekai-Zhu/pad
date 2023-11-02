def solution():
    total_words = 1200  # Keenan needs to write a 1200 word essay
    words_per_hour = [400, 400, 200, 200, 200, 200, 200, 200]  # Keenan writes 400 words per hour for the first two hours, then 200 words per hour
    hours_left = 0  # hours_left will keep track of the remaining hours

    # Loop through the words_per_hour list to determine how many hours Keenan needs to finish the essay
    for i in range(len(words_per_hour)):
        if total_words > 0:
            total_words -= words_per_hour[i]
            hours_left += 1
        else:
            break
    
    result = hours_left
    return result

print(solution())