def solution():
    """Jenna is making a costume for her role in Oliver Twist. She needs to make an overskirt and two petticoats. Each skirt uses a rectangle of material that measures 12 feet by 4 feet. She also needs to make a bodice that uses 2 square feet of material for the shirt and 5 square feet of fabric for each of the sleeves. If the material she uses costs $3 per square foot, how much does she spend on the material in total?"""
    # Calculate the area of each skirt
    skirt_area = 12 * 4

    # Calculate the area of all the skirts
    total_skirt_area = (skirt_area * 3)

    # Calculate the area of the bodice
    bodice_area = (2 + (5 * 2))

    # Calculate the total fabric area
    total_fabric_area = total_skirt_area + bodice_area

    # Calculate the total cost of the fabric
    fabric_cost = total_fabric_area * 3

    # return the result
    result = fabric_cost
    return result

print(solution())