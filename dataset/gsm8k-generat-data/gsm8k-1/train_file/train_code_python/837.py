def solution():
    """A boat carrying 20 sheep, 10 cows and 14 dogs capsized. 3 of the sheep drowned. Twice as many cows drowned as did sheep. All of the dogs made it to shore. How many total animals made it to the shore?"""
    sheep_on_boat = 20
    cows_on_boat = 10
    dogs_on_boat = 14
    sheep_drowned = 3
    cows_drowned = 2 * sheep_drowned
    total_animals_on_boat = sheep_on_boat + cows_on_boat + dogs_on_boat
    animals_lost = sheep_drowned + cows_drowned
    animals_saved = total_animals_on_boat - animals_lost - dogs_on_boat
    result = animals_saved
    return result

print(solution())