def solution():
    """Katy, Wendi, and Carrie went to a bread-making party. Katy brought three 5-pound bags of flour. Wendi brought twice as much flour as Katy, but Carrie brought 5 pounds less than the amount of flour Wendi brought. How much more flour, in ounces, did Carrie bring than Katy?"""
    
    # Define the amount of flour Katy brought
    katy_flour = 3 * 5 * 16  # 5-pound bags converted to ounces

    # Define the amount of flour Wendi brought (twice as much as Katy)
    wendi_flour = katy_flour * 2

    # Define the amount of flour Carrie brought (5 pounds less than Wendi)
    carrie_flour = wendi_flour - 5 * 16  # 5 pounds converted to ounces

    # Calculate the difference in flour brought between Carrie and Katy
    flour_difference = carrie_flour - katy_flour

    result = flour_difference
    return result

print(solution())