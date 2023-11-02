def solution():
    """One barnyard owl makes 5 hoot sounds per minute.  If 5 less than 20 hoots per minute are heard coming out of the barn, how many Barnyard owls would this noise be coming from?"""
    # Define the number of hoots per minute made by one Barnyard owl
    HOOTS_PER_MINUTE = 5

    # Define the total number of hoots per minute heard from the barn
    total_hoots = 20 - 5

    # Calculate the number of Barnyard owls making the hoot sounds
    num_owls = total_hoots / HOOTS_PER_MINUTE

    # Display the number of Barnyard owls
    result = num_owls
    return result

print(solution())