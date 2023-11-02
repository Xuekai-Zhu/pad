def solution():
    total_seagulls = 36  # There are 36 seagulls on the roof

    # Calculate the number of seagulls scared away by the kids
    scared_seagulls = total_seagulls / 4

    # Calculate the number of remaining seagulls
    remaining_seagulls = total_seagulls - scared_seagulls

    # Calculate the number of seagulls that fly to McDonald's
    flown_seagulls = remaining_seagulls / 3

    # Calculate the number of seagulls left on the roof
    left_seagulls = remaining_seagulls - flown_seagulls
    result = left_seagulls
    return result

print(solution())