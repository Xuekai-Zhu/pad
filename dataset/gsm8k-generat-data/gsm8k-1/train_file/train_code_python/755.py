def solution():
    """Anna, Alison, and Jeff collect stamps. Anna had 37 stamps in her collection, Alison had 28 stamps in her collection, and Jeff had 31 stamps in his collection. Alison gave Anna half of her collection in exchange for a novel,
    and then Anna traded Jeff two bluebird stamps for one mountain stamp. How many stamps did Anna have in the end?"""
    
    # Initial stamp counts
    anna_stamps = 37
    alison_stamps = 28
    jeff_stamps = 31
    
    # Alison gives half of her stamps to Anna
    alison_stamps_given = alison_stamps / 2
    anna_stamps += alison_stamps_given
    
    # Anna trades Jeff two bluebird stamps for one mountain stamp
    bluebird_stamps_traded = 2
    mountain_stamps_traded = 1
    anna_stamps -= bluebird_stamps_traded
    jeff_stamps += bluebird_stamps_traded
    jeff_stamps -= mountain_stamps_traded
    anna_stamps += mountain_stamps_traded
    
    result = anna_stamps
    return result

print(solution())