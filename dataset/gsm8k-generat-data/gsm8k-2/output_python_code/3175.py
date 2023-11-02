def solution():
    """Cynthia has three children whose ages add up to 35. Matthew is two years older than Rebecca and four years younger than Freddy. How many years old is Freddy?"""
    total_age = 35
    # Let's assume Rebecca's age is x
    rebecca_age = (total_age - 2) / 3
    # Matthew is two years older than Rebecca
    matthew_age = rebecca_age + 2
    # Freddy is four years younger than Matthew
    freddy_age = matthew_age - 4
    result = freddy_age
    return result

print(solution())