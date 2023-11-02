def solution():
    """Cynthia has three children whose ages add up to 35. Matthew is two years older than Rebecca and four years younger than Freddy. How many years old is Freddy?"""
    total_age = 35
    rebecca_age = (total_age - 2 - 4) / 3
    freddy_age = rebecca_age + 4
    result = freddy_age
    return result

print(solution())