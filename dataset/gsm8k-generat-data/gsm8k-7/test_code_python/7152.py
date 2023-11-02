def solution():
    blanche_green = 12
    blanche_red = 3

    rose_red = 9
    rose_blue = 11

    dorothy_red = 2*(blanche_red + rose_red)
    dorothy_blue = 3*rose_blue

    total_dorothy = dorothy_red + dorothy_blue
    result = total_dorothy
    return result

print(solution())