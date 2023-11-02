def solution():
    staplers_in_box = 50
    stapled_reports = 3
    staples_per_report = 36
    total_stapled = stapled_reports * staples_per_report
    staplers_left = staplers_in_box - total_stapled
    result = staplers_left
    return result

print(solution())