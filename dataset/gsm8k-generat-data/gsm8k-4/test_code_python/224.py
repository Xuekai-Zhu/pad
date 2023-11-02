def solution():
    """A library cabinet houses five ancient scrolls. The first scroll is 4080 years old. If each scroll is older than the last by half as many years as the last scroll’s age, how old is the fifth scroll?"""
    # Define the age of the first scroll
    first_scroll_age = 4080

    # Calculate the age of the second scroll
    second_scroll_age = first_scroll_age + (0.5 * first_scroll_age)

    # Calculate the age of the third scroll
    third_scroll_age = second_scroll_age + (0.5 * second_scroll_age)

    # Calculate the age of the fourth scroll
    fourth_scroll_age = third_scroll_age + (0.5 * third_scroll_age)

    # Calculate the age of the fifth scroll
    fifth_scroll_age = fourth_scroll_age + (0.5 * fourth_scroll_age)

    result = fifth_scroll_age
    return result

print(solution())