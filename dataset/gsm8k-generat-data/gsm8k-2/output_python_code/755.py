def solution():
    """Anna, Alison, and Jeff collect stamps. Anna had 37 stamps in her collection, Alison had 28 stamps in her collection, and Jeff had 31 stamps in his collection. Alison gave Anna half of her collection in exchange for a novel, and then Anna traded Jeff two bluebird stamps for one mountain stamp. How many stamps did Anna have in the end?"""
    anna_stamps = 37
    alison_stamps = 28
    jeff_stamps = 31

    # Alison gives half her collection to Anna
    alison_stamps /= 2
    anna_stamps += alison_stamps

    # Anna trades 2 bluebird stamps for 1 mountain stamp with Jeff
    anna_stamps -= 2
    jeff_stamps -= 1
    anna_stamps += 1

    result = anna_stamps
    return result

print(solution())