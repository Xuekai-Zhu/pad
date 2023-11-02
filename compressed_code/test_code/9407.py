def solution():
    
    total_pages = 400
    percent_finished = 20
    pages_finished = total_pages * (percent_finished / 100)
    pages_left = total_pages - pages_finished
    result = pages_left
    return result

print(solution())