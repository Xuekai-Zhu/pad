def solution():
    # Calculate the total number of hushpuppies needed
    total_hushpuppies = 5 * 20  # each guest will eat 5 hushpuppies and there are 20 guests

    # Calculate the time it will take to cook all the hushpuppies
    time_per_hushpuppy = 8 / 10  # It takes 8 minutes to cook 10 hushpuppies
    total_time = time_per_hushpuppy * total_hushpuppies
    result = total_time
    return result

print(solution())