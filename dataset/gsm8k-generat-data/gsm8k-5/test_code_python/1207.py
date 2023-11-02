def solution():
    seashells_first_day = 5  # Nala found 5 seashells on the first day
    seashells_second_day = 7  # Nala found 7 seashells on the second day
    seashells_third_day = seashells_first_day * 2  # Nala found twice the number she got from the first two days

    # Calculate the total number of seashells Nala has
    total_seashells = seashells_first_day + seashells_second_day + seashells_third_day
    result = total_seashells
    return result

print(solution())