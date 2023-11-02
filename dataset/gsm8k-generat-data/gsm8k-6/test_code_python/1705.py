def solution():
    #calculate the total number of flowers Maria will have
    dozens = 3
    flowers = dozens * 12
    free_flowers = (dozens // 1) * 2
    total_flowers = flowers + free_flowers
    result = total_flowers
    return result

print(solution())