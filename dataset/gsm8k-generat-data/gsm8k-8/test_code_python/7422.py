def solution():
    punch_bowl_capacity = 16

    # Calculate the amount of punch remaining after Mark's cousin drank half
    remaining_punch_after_cousin = punch_bowl_capacity / 2

    # Calculate the amount of punch Mark added before his cousin drank
    initial_punch_added = remaining_punch_after_cousin - 4

    # Calculate the amount of punch remaining after Sally drank
    remaining_punch_after_sally = remaining_punch_after_cousin - 2

    # Calculate the total amount of punch Mark had to add to completely fill the bowl
    total_punch_added = punch_bowl_capacity - remaining_punch_after_sally

    # Calculate the amount of punch Mark initially added
    initial_punch_added = total_punch_added - 12

    result = initial_punch_added
    return result

print(solution())