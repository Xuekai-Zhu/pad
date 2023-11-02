def solution():
    """Hasan is packing up his apartment because he’s moving across the country for a new job. He needs to ship several boxes to his new home. The movers have asked that Hasan avoid putting more than a certain weight in pounds in any cardboard box. The moving company has helpfully provided Hasan with a digital scale that will alert him if a package is too heavy. Hasan is in the kitchen, and he fills a cardboard box with 38 dinner plates. When he checks the box, the scale reports his box is too heavy. Hasan knows each of his plates weighs 10 ounces. He removes a single plate from the box and checks the movers’ scale again. The scale reports his box is still too heavy. Hasan repeats the process again and again. When he has removed enough plates, the movers’ scale shows the box is now an acceptable weight for shipping. Hasan deduces that each shipping box can hold 20 pounds before the scale says the box is too heavy.  How many plates did Hasan need to remove from the shipping box?"""
    # Define the weight of each plate in pounds
    PLATE_WEIGHT = 10 / 16  # 10 ounces is 1/16 of a pound

    # Define the maximum weight of the shipping box in pounds
    MAX_WEIGHT = 20

    # Define the number of plates initially in the box
    initial_plates = 38

    # Calculate the initial weight of the box in pounds
    initial_weight = initial_plates * PLATE_WEIGHT

    # Calculate the number of plates that need to be removed
    plates_removed = 0
    while (initial_weight + plates_removed * PLATE_WEIGHT) > MAX_WEIGHT:
        plates_removed += 1

    # Display the number of plates that need to be removed
    result = plates_removed
    return result

print(solution())