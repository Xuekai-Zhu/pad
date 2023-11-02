def solution():
    biggest_doll = 243
    size_reduction = 2/3
    size_of_sixth_doll = biggest_doll * (size_reduction ** 5)
    result = size_of_sixth_doll
    return result

print(solution())