def solution():
    starting_amount = 65
    used_amount = 18
    bought_amount = 50

    # Calculate Jack's sugar amount after using some
    after_use = starting_amount - used_amount

    # Calculate Jack's sugar amount after buying more
    end_amount = after_use + bought_amount
    result = end_amount
    return result

print(solution())