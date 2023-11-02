def solution():
    """A library cabinet houses five ancient scrolls. The first scroll is 4080 years old. If each scroll is older than the last by half as many years as the last scroll’s age, how old is the fifth scroll?"""
    first_scroll_age = 4080
    second_scroll_age = first_scroll_age + (0.5 * first_scroll_age)
    third_scroll_age = second_scroll_age + (0.5 * second_scroll_age)
    fourth_scroll_age = third_scroll_age + (0.5 * third_scroll_age)
    fifth_scroll_age = fourth_scroll_age + (0.5 * fourth_scroll_age)
    result = fifth_scroll_age
    return result

print(solution())