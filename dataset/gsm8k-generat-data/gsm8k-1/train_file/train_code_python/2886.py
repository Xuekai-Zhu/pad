def solution():
    """Cara is at her family reunion, where she discovers that she is 20 years younger than her mom. Her mom is 15 years younger than Cara's Grandmother. If Cara's grandmother is 75, how old is Cara?"""
    grandmother_age = 75
    mom_age = grandmother_age - 15
    cara_age = mom_age - 20
    result = cara_age
    return result

print(solution())