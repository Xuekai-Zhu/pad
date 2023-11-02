def solution():
    """When you take Hiram's age and then add 12, you get 4 less than twice Allyson's age. If Hiram is 40 years old, how old is Allyson?"""
    hiram_age = 40
    allyson_age = (hiram_age + 12 + 4) / 2
    result = allyson_age
    return result

print(solution())