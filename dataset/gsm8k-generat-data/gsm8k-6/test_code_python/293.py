def solution():
    # Calculate the time Carlotta spends practicing, tantruming, and singing during the final performance
    singing_time = 6  # given
    practicing_time = 3 * singing_time  # for every 1 minute singing, she spends an additional 3 minutes practicing
    tantruming_time = 5 * singing_time  # for every 1 minute singing, she spends an additional 5 minutes throwing tantrums
    total_time = singing_time + practicing_time + tantruming_time

    result = total_time
    return result

print(solution())