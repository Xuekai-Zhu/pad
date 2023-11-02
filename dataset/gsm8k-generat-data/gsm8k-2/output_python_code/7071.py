def solution():
    """In 5 years, Nacho will be three times older than Divya. If Divya is currently 5 years old, what's the sum of their ages now?"""
    divya_age = 5
    nacho_age = 3 * (divya_age + 5) - 5
    total_age = divya_age + nacho_age
    result = total_age
    return result

print(solution())