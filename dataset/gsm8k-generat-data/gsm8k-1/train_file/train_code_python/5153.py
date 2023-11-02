def solution():
    """Thomas is 6 years old. His older sister, Shay, is 13 years older than him and 5 years younger than their older brother, James. How old will James be by the time Thomas reaches his current age?"""
    thomas_age = 6
    shay_age = thomas_age + 13
    james_age = shay_age + 5
    time_diff = james_age - thomas_age
    result = time_diff
    return result

print(solution())