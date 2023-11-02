def solution():
    """Anna, Alison, and Jeff collect stamps. Anna had 37 stamps in her collection, Alison had 28 stamps in her collection, and Jeff had 31 stamps in his collection. Alison gave Anna half of her collection in exchange for a novel, and then Anna traded Jeff two bluebird stamps for one mountain stamp. How many stamps did Anna have in the end?"""
    # Define the initial number of stamps for each collector
    anna_stamps = 37
    alison_stamps = 28
    jeff_stamps = 31

    # Calculate the new number of stamps for Anna after Alison gave her half of her collection
    alison_half = alison_stamps // 2
    anna_stamps += alison_half

    # Calculate the new number of stamps for Jeff after Anna traded 2 bluebird stamps for 1 mountain stamp
    jeff_bluebird = 2
    jeff_mountain = 1
    anna_bluebird = jeff_bluebird
    jeff_bluebird -= 2
    jeff_mountain += 1
    anna_stamps -= 2
    anna_stamps += jeff_mountain

    # return the result
    result = anna_stamps
    return result

print(solution())