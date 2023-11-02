def solution():

    horses = 2
    dogs = 5
    cats = 7
    turtles = 3
    goat = 1

    legs_per_horse = 4
    legs_per_dog = 4
    legs_per_cat = 4
    legs_per_turtle = 2
    legs_per_goat = 4

    total_legs = (horses * legs_per_horse) + (dogs * legs_per_dog) + (cats * legs_per_cat) + (turtles * legs_per_turtle) + (goat * legs_per_goat)
    result = total_legs
    
    return result

print(solution())