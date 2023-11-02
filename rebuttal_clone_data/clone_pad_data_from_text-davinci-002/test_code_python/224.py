def solution():
    """A library cabinet houses five ancient scrolls. The first scroll is 4080 years old. If each scroll is older than the last by half as many years as the last scroll’s age, how old is the fifth scroll?"""
    first_scroll_age = 4080
    age_difference = first_scroll_age / 2
    fifth_scroll_age = first_scroll_age + (age_difference * 4)
    result = fifth_scroll_age
    return result

print(solution())