def solution():
    total_fruit = 10
    fruit_kept = 2
    fruit_brought_friday = 3

    # Calculate the total fruit eaten in the first four days
    fruit_eaten_first_four = total_fruit - fruit_kept - fruit_brought_friday
    result = fruit_eaten_first_four
    return result

print(solution())