def solution():
    difference_jenny_charlie = 5
    difference_charlie_bobby = 3
    jenny_twice_as_old = difference_jenny_charlie + (difference_charlie_bobby * 2)
    charlie_twice_as_old = jenny_twice_as_old - difference_jenny_charlie
    result = charlie_twice_as_old
    return result

print(solution())