def solution():
    # Calculate the total time of the album in seconds
    total_time = 3.5 * 60 * 10  # 3.5 minutes converted to seconds, multiplied by 10 songs

    # Calculate the number of times Lucy will jump rope
    jumps = total_time // 1  # integer division to get the number of whole seconds
    result = jumps
    return result

print(solution())