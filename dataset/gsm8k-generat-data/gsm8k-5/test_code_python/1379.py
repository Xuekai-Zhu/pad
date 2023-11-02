def solution():
    # Calculate the number of kittens born in the first spring
    breeding_rabbits = 10
    kittens_first_spring = breeding_rabbits * 10
    adopted_kittens = kittens_first_spring / 2
    returned_kittens = 5
    remaining_kittens = kittens_first_spring - adopted_kittens - returned_kittens

    # Calculate the number of rabbits Lola has after the first spring
    total_rabbits = breeding_rabbits + remaining_kittens

    # Calculate the number of kittens born in the second spring
    kittens_second_spring = 60
    adopted_kittens = 4
    remaining_kittens = kittens_second_spring - adopted_kittens

    # Calculate the total number of rabbits Lola has after the second spring
    total_rabbits += remaining_kittens

    result = total_rabbits
    return result

print(solution())