def solution(week):
    if week == 1:
        return 4
    else:
        return 2*solution(week-1) 
    
solution(5)

print(solution())