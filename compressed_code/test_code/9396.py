def solution():
    
    eggs = 60
    toilet_paper = 7
    egg_cleanup_time = eggs * 15/60
    toilet_paper_cleanup_time = toilet_paper * 30
    total_cleanup_time = egg_cleanup_time + toilet_paper_cleanup_time
    result = total_cleanup_time

    return result

print(solution())