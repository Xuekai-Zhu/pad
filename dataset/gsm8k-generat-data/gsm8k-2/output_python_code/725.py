def solution():
    """Jed is 10 years older than Matt. In 10 years, Jed will be 25 years old. What is the sum of their present ages?"""
    jed_future_age = 25
    jed_current_age = jed_future_age - 10
    matt_current_age = jed_current_age - 10
    total_age = jed_current_age + matt_current_age
    result = total_age
    return result

print(solution())