def solution():
    """In four years, Annika will be three times as old as Hans. If Hans is now 8 years old, how old is Annika now?"""
    hans_age = 8
    annika_future_age = hans_age * 3
    annika_current_age = annika_future_age - 4
    result = annika_current_age
    return result

print(solution())