def solution():
    # Calculate the total number of baby mice
    total_babies = 3 * 8

    # Calculate the number of mice given to Robbie
    robbie_mice = total_babies / 6

    # Calculate the number of mice sold to the pet store
    pet_store_mice = 3 * robbie_mice

    # Calculate the number of mice remaining
    remaining_mice = total_babies - robbie_mice - pet_store_mice

    # Calculate the number of mice sold to snake owners
    snake_mice = remaining_mice / 2

    # Calculate the number of baby mice Brenda has left
    left_over = remaining_mice - snake_mice

    result = left_over
    return result

print(solution())