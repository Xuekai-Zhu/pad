def solution():
    jokes_told_1 = 11
    jokes_told_2 = 7
    total_jokes = jokes_told_1 + jokes_told_2
    jokes_told_1_next = jokes_told_1 * 2
    jokes_told_2_next = jokes_told_2 * 2
    total_jokes_next = jokes_told_1_next + jokes_told_2_next
    total_jokes_so_far = total_jokes + total_jokes_next
    result = total_jokes_so_far
    return result

print(solution())