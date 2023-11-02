def solution():
    num_crates_tuesday = 6
    num_crates_thursday = 5
    num_eggs_per_crate = 30
    num_eggs_given_away = 2*num_eggs_per_crate  # Susan was given 2 crates

    # Calculate the total number of eggs Michael has now
    total_eggs = (num_crates_tuesday + num_crates_thursday)*num_eggs_per_crate - num_eggs_given_away
    result = total_eggs
    return result

print(solution())