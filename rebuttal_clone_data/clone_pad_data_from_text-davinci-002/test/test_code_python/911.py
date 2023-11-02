def solution():
    oranges_needed_1 = 20
    oranges_needed_2 = oranges_needed_1 * 2
    oranges_picked = 90
    oranges_remaining = oranges_picked - (oranges_needed_1 + oranges_needed_2)
    result = oranges_remaining
    return result

print(solution())