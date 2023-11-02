def solution():
    """A zoo is arranging the layout of its animal enclosures. There are 4 tiger enclosures in a row and behind each of these are 2 zebra enclosures. There are three times as many giraffe enclosures as zebra enclosures scattered around the zoo. The tiger enclosures hold 4 tigers, the zebra enclosures hold 10 zebras and the giraffe enclosures hold 2 giraffes. If these are the only animals in the zoo, how many animals are in the zoo?"""
    tigers = 4 * 4
    zebras = 2 * 4 * 10
    giraffes = 3 * zebras * 2
    total_animals = tigers + zebras + giraffes
    result = total_animals
    return result

print(solution())