def solution():
    # Initial number of dogs at the rescue center
    total_dogs = 200

    # Number of dogs to be moved in
    moved_dogs = 100

    # Total number of dogs after the move
    total_dogs += moved_dogs

    # Dogs given out for adoption after a week
    dogs_adopted_week1 = 40
    total_dogs -= dogs_adopted_week1

    # Dogs adopted after a month
    dogs_adopted_month1 = 60
    total_dogs -= dogs_adopted_month1

    result = total_dogs
    return result

print(solution())