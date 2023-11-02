def solution():
    karen_quarters = 32
    christopher_quarters = 64

    # Calculate the total value of Karen's quarters
    karen_value = karen_quarters * 0.25

    # Calculate the total value of Christopher's quarters
    christopher_value = christopher_quarters * 0.25

    # Calculate how much more money Christopher has than Karen
    difference = christopher_value - karen_value
    result = difference
    return result

print(solution())