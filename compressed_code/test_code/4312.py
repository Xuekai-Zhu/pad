def solution():
    
    biff_voters = 0.45 * 200
    undecided_voters = 0.08 * 200
    marty_voters = 200 - biff_voters - undecided_voters
    result = marty_voters
    return result

print(solution())