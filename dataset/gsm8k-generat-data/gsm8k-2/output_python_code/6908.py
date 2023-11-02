def solution():
    """If 8 carpenters can make 50 chairs in 10 days, how many carpenters are needed to make 75 chairs in 10 days?"""
    carpenters = 8
    chairs = 50
    days = 10
    chairs_per_day = chairs / days
    target_chairs = 75
    target_carpenters = (target_chairs / chairs_per_day) * (carpenters / 1)  # Use cross-multiplication
    result = target_carpenters
    return result

print(solution())