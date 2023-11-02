def solution():
    """Harry slept 9 hours last night. His friend James slept only 2/3 of what Harry slept. How many more hours did Harry sleep than James?"""
    harry_sleep = 9
    james_sleep = harry_sleep * (2/3)
    difference = harry_sleep - james_sleep
    result = difference
    return result

print(solution())