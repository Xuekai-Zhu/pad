def solution():
    """Artemis is potting flowers with her father. They buy a 30-pound bag of soil. Each rose needs 1 pound. Each carnation needs 1.5 pounds. Each Sunflower needs 3 pounds. If they plant 4 sunflowers and 10 carnations, how many roses can they plant?"""
    bag_of_soil = 30
    sunflowers = 4
    sunflower_weight = 3
    carnations = 10
    carnation_weight = 1.5
    roses_weight = sunflowers * sunflower_weight + carnations * carnation_weight
    roses_planted = bag_of_soil - roses_weight
    result = roses_planted
    return result

print(solution())