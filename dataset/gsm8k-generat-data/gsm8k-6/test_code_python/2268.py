def solution():
    # Calculate the total time Kevin spends finding worms
    total_time = 6 * 60  # 6 hours in minutes

    # Calculate the number of worms Kevin finds in the total time
    worms_found = total_time // 15

    # Calculate the number of toads Kevin has in his shoebox
    toads = worms_found // 3

    result = toads
    return result

print(solution())