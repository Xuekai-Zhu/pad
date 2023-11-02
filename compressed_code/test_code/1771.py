def solution():
    
    last_year_signups = 200
    no_show = 40
    actual_runners = last_year_signups - no_show
    this_year_runners = actual_runners * 2
    result = this_year_runners
    return result

print(solution())