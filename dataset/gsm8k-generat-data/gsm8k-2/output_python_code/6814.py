def solution():
    """A zoo is arranging the layout of its animal enclosures. There are 4 tiger enclosures in a row and behind each of these are 2 zebra enclosures. There are three times as many giraffe enclosures as zebra enclosures scattered around the zoo. The tiger enclosures hold 4 tigers, the zebra enclosures hold 10 zebras and the giraffe enclosures hold 2 giraffes. If these are the only animals in the zoo, how many animals are in the zoo?"""
    tiger_enclosures = 4
    zebra_enclosures = tiger_enclosures * 2
    giraffe_enclosures = zebra_enclosures * 3
    total_tigers = tiger_enclosures * 4
    total_zebras = zebra_enclosures * 10
    total_giraffes = giraffe_enclosures * 2
    total_animals = total_tigers + total_zebras + total_giraffes
    result = total_animals
    return result

print(solution())