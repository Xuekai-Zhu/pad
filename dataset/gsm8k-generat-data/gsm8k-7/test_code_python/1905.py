def solution():
    total_pipe_length = 40
    bolt_spacing = 5
    washers_per_bolt = 2
    total_washers = 20

    # Calculate the total number of bolts needed
    bolts_needed = total_pipe_length / bolt_spacing

    # Calculate the total number of washers needed
    washers_needed = bolts_needed * washers_per_bolt

    # Calculate the number of washers remaining in the bag
    washers_remaining = total_washers - washers_needed
    result = washers_remaining
    return result

print(solution())