def solution():
    """A doctor needs to give medicine to a child, and he knows that he cannot give the same amount of medicine that he would give to an adult. The instructions say that for every kilogram of weight the child must be given 5 ml of medicine. The doctor knows that the child weighs 30 kilograms and that also the full dose has to be given in 3 equal parts. How many milligrams will each part of the dose be?"""
    weight = 30
    dose = weight * 5
    parts = 3
    dose_per_part = dose / parts
    result = dose_per_part
    return result

print(solution())