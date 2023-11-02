def solution():
    """Jenna is making a costume for her role in Oliver Twist. She needs to make an overskirt and two petticoats. Each skirt uses a rectangle of material that measures 12 feet by 4 feet. She also needs to make a bodice that uses 2 square feet of material for the shirt and 5 square feet of fabric for each of the sleeves. If the material she uses costs $3 per square foot, how much does she spend on the material in total?"""
    
    # Calculate the area of the material needed for each skirt
    skirt_area = 12 * 4

    # Calculate the total area of the material needed for the overskirt and two petticoats
    total_skirt_area = 3 * skirt_area

    # Calculate the area of the material needed for the bodice
    bodice_area = 2 + (5 * 2)

    # Calculate the total area of the material needed for the entire costume
    total_area = total_skirt_area + bodice_area

    # Calculate the total cost of the material
    total_cost = total_area * 3

    # Display the total cost
    result = total_cost
    return result

print(solution())