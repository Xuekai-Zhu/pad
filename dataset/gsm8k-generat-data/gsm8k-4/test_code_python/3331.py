def solution():
    """Hasan is packing up his apartment because he’s moving across the country for a new job. He needs to ship several boxes to his new home. The movers have asked that Hasan avoid putting more than a certain weight in pounds in any cardboard box. The moving company has helpfully provided Hasan with a digital scale that will alert him if a package is too heavy. Hasan is in the kitchen, and he fills a cardboard box with 38 dinner plates. When he checks the box, the scale reports his box is too heavy. Hasan knows each of his plates weighs 10 ounces. He removes a single plate from the box and checks the movers’ scale again. The scale reports his box is still too heavy. Hasan repeats the process again and again. When he has removed enough plates, the movers’ scale shows the box is now an acceptable weight for shipping. Hasan deduces that each shipping box can hold 20 pounds before the scale says the box is too heavy. How many plates did Hasan need to remove from the shipping box?"""
    # Define the weight limit in pounds
    weight_limit = 20

    # Convert the weight of one plate from ounces to pounds
    plate_weight = 10 / 16

    # Define the number of plates originally in the box
    plates_original = 38

    # Calculate the weight of the original box in pounds
    weight_original = plates_original * plate_weight

    # Keep removing one plate at a time until the weight is below the limit
    plates_removed = 0
    while weight_original > weight_limit:
        plates_removed += 1
        plates_original -= 1
        weight_original = plates_original * plate_weight

    # Return the number of plates removed
    result = plates_removed
    return result

print(solution())