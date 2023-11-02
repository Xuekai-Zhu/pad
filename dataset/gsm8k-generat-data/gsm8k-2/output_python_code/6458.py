def solution():
    """Juliet is 3 years older than her sister Maggie but 2 years younger than her elder brother Ralph. If Juliet is 10 years old, what is the sum of Maggie's and Ralph's ages?"""
    juliet_age = 10
    maggie_age = juliet_age - 3
    ralph_age = juliet_age + 2
    total_age = maggie_age + ralph_age
    result = total_age
    return result

print(solution())