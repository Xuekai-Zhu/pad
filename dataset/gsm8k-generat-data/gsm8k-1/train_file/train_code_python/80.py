def solution():
    """Sam and Jeff had a skipping competition at recess. The competition was split into four rounds. Sam completed 1 more skip than Jeff in the first round. Jeff skipped 3 fewer times than Sam in the second round. Jeff skipped 4 more times than Sam in the third round. Jeff got tired and only completed half the number of skips as Sam in the last round. If Sam skipped 16 times in each round, what is the average number of skips per round completed by Jeff?"""
    sam_rounds = [16, 16, 16, 16]
    jeff_rounds = []
    
    # calculate Jeff's skips in each round
    jeff_rounds.append(sam_rounds[0]-1)
    jeff_rounds.append(sam_rounds[1]-3)
    jeff_rounds.append(sam_rounds[2]+4)
    jeff_rounds.append(sam_rounds[3]/2)
    
    # calculate average of Jeff's skips per round
    avg_jeff_skips = sum(jeff_rounds)/len(jeff_rounds)
    
    result = avg_jeff_skips
    return result

print(solution())