def solution():
    """Teresa is collecting pencils. She has 14 colored pencils and 35 black pencils. Her three younger siblings need pencils for class and their dad asks her to share all her pencils, giving each an equal number of pencils, regardless of color. He tells her she can keep 10 of them for herself. How many pencils does each sibling get?"""
    # Define the number of colored and black pencils
    colored_pencils = 14
    black_pencils = 35

    # Calculate the total number of pencils
    total_pencils = colored_pencils + black_pencils

    # Subtract the number of pencils that Teresa is keeping for herself
    total_pencils -= 10

    # Divide the remaining pencils equally among the 3 siblings
    pencils_per_sibling = total_pencils // 3

    # Return the result
    result = pencils_per_sibling
    return result

print(solution())