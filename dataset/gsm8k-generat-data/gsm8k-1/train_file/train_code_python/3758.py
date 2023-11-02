def solution():
    """A van is delivering 180 bottles of drinks to a neighborhood, and each bottle contains either cider or beer or a mixture of the two. Out of the 180 bottles, 40 contain only cider, 80 contain only beer, and the rest are a mixture of the two drinks. If the delivery man gives half the number of each bottle of drink to the first house, how many bottles does the first house get?"""
    total_bottles = 180
    cider_bottles = 40
    beer_bottles = 80
    mixed_bottles = total_bottles - cider_bottles - beer_bottles
    first_house_bottles = (cider_bottles + beer_bottles + mixed_bottles) / 2
    result = first_house_bottles
    return result

print(solution())