def solution():
    """One barnyard owl makes 5 hoot sounds per minute. If 5 less than 20 hoots per minute are heard coming out of the barn, how many Barnyard owls would this noise be coming from?"""
    # Define the number of hoot sounds heard per minute
    total_hoots_per_minute = 20 - 5

    # Calculate the number of barnyard owls based on the number of hoot sounds heard
    num_owls = total_hoots_per_minute / 5

    result = num_owls
    return result

print(solution())