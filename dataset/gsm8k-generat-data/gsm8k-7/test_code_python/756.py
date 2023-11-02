def solution():
    anna = 37
    alison = 28
    jeff = 31

    # Alison gave half of her collection to Anna
    anna += alison/2
    alison /= 2

    # Anna traded Jeff 2 bluebird stamps for 1 mountain stamp
    anna -= 2
    jeff -= 1
    anna += 1

    result = anna
    return result

print(solution())