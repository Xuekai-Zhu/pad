def solution():
    """Darcie is 4 years old. She is 1/6 as old as her mother and her mother is 4/5 as old as her father. How old is her father?"""
    darcie_age = 4
    mother_age = darcie_age * 6
    father_age = mother_age * 5 / 4
    result = father_age
    return result

print(solution())