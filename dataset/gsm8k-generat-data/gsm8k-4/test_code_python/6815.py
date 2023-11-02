def solution():
    """A zoo is arranging the layout of its animal enclosures. There are 4 tiger enclosures in a row and behind each of these are 2 zebra enclosures. There are three times as many giraffe enclosures as zebra enclosures scattered around the zoo. The tiger enclosures hold 4 tigers, the zebra enclosures hold 10 zebras and the giraffe enclosures hold 2 giraffes. If these are the only animals in the zoo, how many animals are in the zoo?"""
    # Calculate the number of zebra enclosures
    zebra_enclosures = 4 * 2

    # Calculate the number of giraffe enclosures
    giraffe_enclosures = 3 * zebra_enclosures

    # Calculate the total number of animals
    tiger_animals = 4 * 4
    zebra_animals = zebra_enclosures * 10
    giraffe_animals = giraffe_enclosures * 2
    total_animals = tiger_animals + zebra_animals + giraffe_animals

    # return the result
    result = total_animals
    return result

print(solution())