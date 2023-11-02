def solution():
    """In eight years, Mr. Bernard will be 3 times as old as Luke is now. If Luke is 20, what is 10 years less than their average age?"""
    luke_age_now = 20
    years_from_now = 8
    mr_bernard_age_from_now = years_from_now * 3
    mr_bernard_age_now = mr_bernard_age_from_now - years_from_now
    total_age = luke_age_now + mr_bernard_age_now
    average_age = total_age / 2
    result = average_age - 10
    return result

print(solution())