def solution():
    # Calculate the number of bottles that are a mixture of cider and beer
    mixed_bottles = 180 - 40 - 80

    # Calculate the number of cider bottles
    cider_bottles = 40 + mixed_bottles / 2

    # Calculate the number of beer bottles
    beer_bottles = 80 + mixed_bottles / 2

    # Calculate the total number of bottles given to the first house
    first_house_bottles = (cider_bottles + beer_bottles) / 2

    result = first_house_bottles
    return result

print(solution())