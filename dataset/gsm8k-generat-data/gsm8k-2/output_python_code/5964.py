def solution():
    """Over several years, Daniel has adopted any stray animals he sees on the side of the road. He now has 2 horses, 5 dogs, 7 cats, 3 turtles, and 1 goat. All of the animals are perfectly healthy. In total, how many legs do his animals have?"""
    horse_legs = 4 * 2
    dog_legs = 4 * 5
    cat_legs = 4 * 7
    turtle_legs = 4 * 3
    goat_legs = 4 * 1
    total_legs = horse_legs + dog_legs + cat_legs + turtle_legs + goat_legs
    result = total_legs
    return result

print(solution())