def solution():
    """Jenna is making a costume for her role in Oliver Twist. She needs to make an overskirt and two petticoats. Each skirt uses a rectangle of material that measures 12 feet by 4 feet. She also needs to make a bodice that uses 2 square feet of material for the shirt and 5 square feet of fabric for each of the sleeves. If the material she uses costs $3 per square foot, how much does she spend on the material in total?"""
    skirt_area = 12 * 4
    bodice_area = 2 + (5 * 2) #shirt + 2 sleeves
    total_area = (skirt_area * 3) + bodice_area
    cost_per_square_foot = 3
    total_cost = total_area * cost_per_square_foot
    result = total_cost
    return result

print(solution())