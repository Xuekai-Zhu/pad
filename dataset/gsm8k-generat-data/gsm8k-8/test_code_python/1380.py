def solution():
    susy_start = 100
    sarah_start = 50

    # Susy's followers after 3 weeks
    susy_end = susy_start + 40 + 20 + 10

    # Sarah's followers after 3 weeks
    sarah_end = sarah_start + 90 + 30 + 10

    # Determine who has the most followers
    if susy_end > sarah_end:
        result = susy_end
    else:
        result = sarah_end
    return result

print(solution())