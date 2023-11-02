def solution():
    # On the first stop, 10 people get on
    current_count = 10

    # On the next stop, 3 people get off and twice as many people get on
    current_count -= 3
    current_count += 2 * 10

    # On the third stop, 18 people get off and 2 get on
    current_count -= 18
    current_count += 2

    result = current_count
    return result

print(solution())