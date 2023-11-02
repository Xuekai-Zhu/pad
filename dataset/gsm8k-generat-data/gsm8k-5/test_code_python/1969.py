def solution():
    starting_amount = 32  # Stacy starts with 32 berries
    taken_amount = 4  # Steve takes 4 of Stacy's berries
    remaining_amount = starting_amount - taken_amount  # Steve has 7 less berries than Stacy started with

    # Calculate how many berries Steve started with
    starting_amount_steve = remaining_amount + 7
    result = starting_amount_steve
    return result

print(solution())