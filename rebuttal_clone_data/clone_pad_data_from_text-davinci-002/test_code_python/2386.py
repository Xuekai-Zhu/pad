def solution():
    cats_in = 12
    cats_already = cats_in / 2
    cats_out = 3 + 1
    cats_new = 5
    cats_now = cats_already + cats_in - cats_out + cats_new
    result = cats_now
    return result

print(solution())