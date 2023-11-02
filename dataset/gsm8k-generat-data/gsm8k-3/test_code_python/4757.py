def solution():
    """Katy, Wendi, and Carrie went to a bread-making party.  Katy brought three 5-pound bags of flour.  Wendi brought twice as much flour as Katy, but Carrie brought 5 pounds less than the amount of flour Wendi brought.  How much more flour, in ounces, did Carrie bring than Katy?"""
    # Define the amount of flour Katy brought
    katy_flour = 3 * 5 * 16 # 3 bags of 5 pounds each, converted to ounces

    # Define the amount of flour Wendi brought
    wendi_flour = 2 * katy_flour

    # Define the amount of flour Carrie brought
    carrie_flour = wendi_flour - 5 * 16 # 5 pounds converted to ounces

    # Calculate how much more flour Carrie brought than Katy
    difference = carrie_flour - katy_flour

    # Display the result
    result = difference
    return result

print(solution())