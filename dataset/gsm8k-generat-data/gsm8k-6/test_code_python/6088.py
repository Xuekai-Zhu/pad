def solution():
    # Calculate the number of shirts Kim's sister takes
    sister_shirts = (1/3) * (4*12)  # Kim has 4 dozen shirts and her sister takes 1/3 of them

    # Calculate the number of shirts left with Kim
    remaining_shirts = (4*12) - sister_shirts  # Kim had 4 dozen shirts and her sister took some of them
    result = remaining_shirts
    return result

print(solution())