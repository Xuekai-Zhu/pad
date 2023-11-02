def solution():
    """In a day, Sam hunts 6 animals. Rob hunts half as many animals as Sam. Mark hunts 1/3 of the total of what Rob and Sam hunt. If Peter hunts 3 times as many animals as Mark does, how many animals do they all hunt in a day?"""
    # Define the number of animals Sam hunts
    sam_animals = 6

    # Calculate the number of animals Rob hunts
    rob_animals = sam_animals / 2

    # Calculate the total number of animals Rob and Sam hunt
    total_animals = sam_animals + rob_animals

    # Calculate the number of animals Mark hunts
    mark_animals = total_animals / 3

    # Calculate the number of animals Peter hunts
    peter_animals = mark_animals * 3

    # Calculate the total number of animals all of them hunt in a day
    total_hunt = sam_animals + rob_animals + mark_animals + peter_animals

    result = total_hunt
    return result

print(solution())