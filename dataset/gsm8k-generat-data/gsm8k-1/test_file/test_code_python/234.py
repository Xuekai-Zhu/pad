def solution():
    """Mary is two years younger than Joan, who is five years older than Jessa. If Jessa is 20 years old, what is the sum of the ages of the three girls?"""
    jessa_age = 20
    joan_age = jessa_age + 5
    mary_age = joan_age - 2
    total_age = jessa_age + joan_age + mary_age
    result = total_age
    
    return result

print(solution())