def solution():
    last_year_runners = 200  # 200 people signed up last year
    no_show_last_year = 40  # 40 people did not show up last year
    runners_this_year = 2 * (last_year_runners - no_show_last_year)  # There will be twice as many runners as last year
    result = runners_this_year
    return result

print(solution())