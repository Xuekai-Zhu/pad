def solution():
    # Find the total time it took Osborn to get dressed from Monday to Thursday
    total_time = 2 + 4 + 3 + 4 

    # Find the time Osborn has to get dressed on Friday to tie his old weekly average 
    time_on_friday = (3*5) - total_time  # multiply the old weekly average by 5 days and subtract the total time for Monday to Thursday
    
    result = time_on_friday
    return result

print(solution())