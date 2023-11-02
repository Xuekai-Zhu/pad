def solution():
    """Thomas is 6 years old. His older sister, Shay, is 13 years older than him and 5 years younger than their older brother, James. How old will James be by the time Thomas reaches his current age?"""
    # Thomas' current age
    thomas_age = 6

    # Shay's age
    shay_age = thomas_age + 13

    # James' age
    james_age = shay_age + 5

    # Years until Thomas reaches James' current age
    years_until = james_age - thomas_age

    # James' age when Thomas reaches his current age
    james_new_age = james_age + years_until

    # Display James' age when Thomas reaches his current age
    result = james_new_age
    return result

print(solution())