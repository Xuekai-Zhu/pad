def solution():
    """Hasan is packing up his apartment because he’s moving across the country for a new job. He needs to ship several boxes to his new home. The movers have asked that Hasan avoid putting more than a certain weight in pounds in any cardboard box. The moving company has helpfully provided Hasan with a digital scale that will alert him if a package is too heavy. Hasan is in the kitchen, and he fills a cardboard box with 38 dinner plates. When he checks the box, the scale reports his box is too heavy. Hasan knows each of his plates weighs 10 ounces. He removes a single plate from the box and checks the movers’ scale again. The scale reports his box is still too heavy. Hasan repeats the process again and again. When he has removed enough plates, the movers’ scale shows the box is now an acceptable weight for shipping. Hasan deduces that each shipping box can hold 20 pounds before the scale says the box is too heavy. How many plates did Hasan need to remove from the shipping box?"""
    plate_weight = 10 / 16  # convert ounces to pounds
    box_weight_limit = 20
    plates_per_box = 38

    current_weight = plates_per_box * plate_weight
    while current_weight > box_weight_limit:
        plates_per_box -= 1
        current_weight = plates_per_box * plate_weight

    removed_plates = 38 - plates_per_box
    result = removed_plates
    return result

print(solution())