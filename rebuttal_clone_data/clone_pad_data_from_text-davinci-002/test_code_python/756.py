def solution():
    original_anna = 37
    original_alison = 28
    original_jeff = 31
    
    alison_gave_anna = original_alison / 2
    anna_gave_jeff = 2
    jeff_gave_anna = 1
    
    anna_total = original_anna + alison_gave_anna - anna_gave_jeff + jeff_gave_anna
    result = anna_total
    return result

print(solution())