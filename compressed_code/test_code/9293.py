def solution():
    
    ahmed_oranges = 8
    hassan_apples = 1
    hassan_oranges = 2
    hassan_total = hassan_apples + hassan_oranges
    ahmed_apples = hassan_apples * 4
    ahmed_total = ahmed_oranges + ahmed_apples
    difference = ahmed_total - hassan_total
    result = difference
    return result

print(solution())