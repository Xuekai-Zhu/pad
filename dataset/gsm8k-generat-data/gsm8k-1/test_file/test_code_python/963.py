def solution():
    """Nani is 8 years old. His brother is twice his age. Nani's sister is 25% younger than him. What is the total age of all three of the family members?"""
    nani_age = 8
    brother_age = nani_age * 2
    sister_age = nani_age - (nani_age * 0.25)
    total_age = nani_age + brother_age + sister_age
    result = total_age
    return result

print(solution())