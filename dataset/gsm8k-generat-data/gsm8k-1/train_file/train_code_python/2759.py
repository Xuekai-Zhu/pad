def solution():
    """Joel is 5 years old and his dad is 32 years old. How old will Joel be when his dad is twice as old as him?"""
    joel_age = 5
    dad_age = 32
    difference = dad_age - joel_age
    age_when_doubled = difference * 2
    years_to_wait = age_when_doubled - difference
    joels_future_age = joel_age + years_to_wait
    result = joels_future_age
    return result

print(solution())