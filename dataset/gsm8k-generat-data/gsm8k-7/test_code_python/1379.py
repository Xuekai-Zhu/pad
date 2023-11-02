def solution():
    num_breeding_rabbits = 10

    # Calculate the number of kittens in the first spring
    num_kittens_first_spring = num_breeding_rabbits * 10

    # Calculate the number of kittens that got adopted and then returned
    num_adopted_first_spring = num_kittens_first_spring / 2
    num_returned_first_spring = 5
    num_kittens_first_spring -= (num_adopted_first_spring - num_returned_first_spring)

    # Calculate the number of kittens in the second spring
    num_kittens_second_spring = 60
    num_adopted_second_spring = 4
    num_kittens_second_spring -= num_adopted_second_spring

    # Calculate the total number of rabbits in Lola's house
    total_rabbits = num_breeding_rabbits + num_kittens_first_spring + num_kittens_second_spring
    result = total_rabbits
    return result

print(solution())