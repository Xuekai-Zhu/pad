def solution():
    
    dancers = 8
    braids_per_dancer = 5
    braid_time = 30 
    total_braids = dancers * braids_per_dancer
    total_time = (total_braids * braid_time) / 60 
    result = total_time
    return result

print(solution())