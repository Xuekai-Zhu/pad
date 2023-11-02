def solution():
    sandwiches_made = 12  # Bert made 12 sandwiches
    sandwiches_eaten_first_day = sandwiches_made / 2  # Bert ate half of the sandwiches on the first day
    sandwiches_eaten_second_day = sandwiches_eaten_first_day - 2  # Bert ate 2 sandwiches less on the second day
    sandwiches_left = sandwiches_made - sandwiches_eaten_first_day - sandwiches_eaten_second_day  # Bert has some sandwiches left

    result = sandwiches_left
    return result

print(solution())