def solution():
    initial_bugs = 400
    sprayed_bugs = initial_bugs * 0.8
    introduced_spiders = 12
    bugs_eaten_by_spiders = introduced_spiders * 7

    total_bugs_left = sprayed_bugs - bugs_eaten_by_spiders
    result = total_bugs_left
    return result

print(solution())