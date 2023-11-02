def solution():
    total_stripes = 13  # Each flag has 13 stripes
    first_stripe_red = True  # The first stripe is red
    remaining_stripes = total_stripes - 1  # Subtracting the first stripe
    half_remaining_red = (remaining_stripes // 2)  # Half of the remaining stripes are red
    red_stripes_per_flag = first_stripe_red + half_remaining_red  # Total number of red stripes in each flag
    num_flags = 10  # John buys 10 flags

    # Calculate the total number of red stripes in all the flags
    total_red_stripes = red_stripes_per_flag * num_flags
    result = total_red_stripes
    return result

print(solution())