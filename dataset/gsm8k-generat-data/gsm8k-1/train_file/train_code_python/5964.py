def solution():
    """
    Over several years, Daniel has adopted any stray animals he sees on the side of the road. 
    He now has 2 horses, 5 dogs, 7 cats, 3 turtles, and 1 goat. All of the animals are perfectly healthy. 
    In total, how many legs do his animals have?
    """
    num_horses = 2
    num_dogs = 5
    num_cats = 7
    num_turtles = 3
    num_goats = 1
    
    legs_per_horse = 4
    legs_per_dog = 4
    legs_per_cat = 4
    legs_per_turtle = 4
    legs_per_goat = 4
    
    total_legs = num_horses * legs_per_horse + num_dogs * legs_per_dog + num_cats * legs_per_cat + num_turtles * legs_per_turtle + num_goats * legs_per_goat
    result = total_legs
    return result

print(solution())