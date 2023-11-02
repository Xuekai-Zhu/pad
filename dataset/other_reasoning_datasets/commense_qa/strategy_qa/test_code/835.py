def solution():
    largest_crustacean_leg_span = 12  # in feet
    king_size_mattress_length = 6.67  # in feet
    if largest_crustacean_leg_span <= king_size_mattress_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())