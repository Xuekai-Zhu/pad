def solution():
    # Calculate the number of pages read by Janet and Belinda in 6 weeks
    janet_pages = 80 * 7 * 6  # number of pages read by Janet in a week multiplied by 6 weeks
    belinda_pages = 30 * 7 * 6  # number of pages read by Belinda in a week multiplied by 6 weeks
    difference = janet_pages - belinda_pages  # calculate the difference in the number of pages read
    result = difference
    return result

print(solution())