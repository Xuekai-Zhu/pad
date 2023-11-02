def solution():
    # Calculate the number of animals in each enclosure
    tigers_per_enclosure = 4
    zebras_per_enclosure = 10
    giraffes_per_enclosure = 2

    # Calculate the total number of enclosures
    tiger_enclosures = 4
    zebra_enclosures = 2 * 4  # 2 zebra enclosures behind each tiger enclosure
    giraffe_enclosures = 3 * 2 * 4  # 3 times as many giraffe enclosures as zebra enclosures
    total_enclosures = tiger_enclosures + zebra_enclosures + giraffe_enclosures

    # Calculate the total number of animals
    total_tigers = tigers_per_enclosure * tiger_enclosures
    total_zebras = zebras_per_enclosure * zebra_enclosures
    total_giraffes = giraffes_per_enclosure * giraffe_enclosures
    total_animals = total_tigers + total_zebras + total_giraffes
    result = total_animals
    return result

print(solution())