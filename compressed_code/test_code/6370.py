def solution():
    
    
    
    anna_stamps = 37
    alison_stamps = 28
    jeff_stamps = 31
    
    
    alison_stamps_given = alison_stamps / 2
    anna_stamps += alison_stamps_given
    
    
    bluebird_stamps_traded = 2
    mountain_stamps_traded = 1
    anna_stamps -= bluebird_stamps_traded
    jeff_stamps += bluebird_stamps_traded
    jeff_stamps -= mountain_stamps_traded
    anna_stamps += mountain_stamps_traded
    
    result = anna_stamps
    return result

print(solution())