def solution():
    biggest_doll = 243  # The biggest doll is 243 cm tall
    size_ratio = 2/3  # Each doll is 2/3rd the size of the doll that contains it

    # Calculate the size of the 6th biggest doll
    sixth_doll_size = biggest_doll * size_ratio ** 5
    result = sixth_doll_size
    return result

print(solution())