def solution():
    eggs = 60
    toilet_paper = 7
    egg_cleanup_time = 15 / 60 # convert seconds to minutes
    tp_cleanup_time = 30
    total_cleanup_time = (eggs * egg_cleanup_time) + (toilet_paper * tp_cleanup_time)
    result = total_cleanup_time
    return result

print(solution())