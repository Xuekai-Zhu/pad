def solution():
    
    sam_rounds = [16, 16, 16, 16]
    jeff_rounds = []
    
    
    jeff_rounds.append(sam_rounds[0]-1)
    jeff_rounds.append(sam_rounds[1]-3)
    jeff_rounds.append(sam_rounds[2]+4)
    jeff_rounds.append(sam_rounds[3]/2)
    
    
    avg_jeff_skips = sum(jeff_rounds)/len(jeff_rounds)
    
    result = avg_jeff_skips
    return result

print(solution())