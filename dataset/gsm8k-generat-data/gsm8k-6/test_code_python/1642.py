def solution():
    # Calculate the length of each essay in words
    johnny_essay = 150
    madeline_essay = 2 * johnny_essay
    timothy_essay = madeline_essay + 30

    # Calculate the total length of all essays in words
    total_length = johnny_essay + madeline_essay + timothy_essay

    # Calculate the number of pages required to accommodate all essays
    pages_needed = total_length // 260 + (total_length % 260 > 0)  # round up to the nearest page

    result = pages_needed
    return result

print(solution())