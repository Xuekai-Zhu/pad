def solution():
    # Calculate the total number of seashells found by Nala in the first two days
    first_two_days = 5 + 7

    # Calculate the number of seashells found on the third day
    third_day = 2 * first_two_days

    # Calculate the total number of seashells found
    total_seashells = first_two_days + third_day

    result = total_seashells
    return result

print(solution())