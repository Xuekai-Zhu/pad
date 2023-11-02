def solution():
    petals_per_ounce = 320
    petals_per_rose = 8
    roses_per_bush = 12
    num_bottles = 20
    ounces_per_bottle = 12

    # Calculate the total number of ounces of perfume needed
    total_ounces = num_bottles * ounces_per_bottle

    # Calculate the total number of roses needed
    total_roses = total_ounces * petals_per_ounce / petals_per_rose

    # Calculate the total number of bushes needed
    total_bushes = total_roses / roses_per_bush
    result = total_bushes
    return result

print(solution())