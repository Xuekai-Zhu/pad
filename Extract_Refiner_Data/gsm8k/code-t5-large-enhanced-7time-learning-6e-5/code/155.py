def solution():
    
    initial_tadpoles = 11
    lily_pad_tadpoles = 6
    rock_tadpoles = 2
    remaining_tadpoles = initial_tadpoles - lily_pad_tadpoles - rock_tadpoles
    result = remaining_tadpoles
    return result

print(solution())