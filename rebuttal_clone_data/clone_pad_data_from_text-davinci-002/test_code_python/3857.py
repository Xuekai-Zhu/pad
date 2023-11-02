def solution():
    pass_attempts = 80
    percent_not_throwing = 30
    not_throwing_attempts = pass_attempts * (percent_not_throwing / 100)
    percent_sacked = 50
    times_sacked = not_throwing_attempts * (percent_sacked / 100)
    result = times_sacked
    return result

print(solution())