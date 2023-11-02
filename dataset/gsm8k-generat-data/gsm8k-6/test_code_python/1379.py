def solution():
    # Calculate the number of kittens born in the first spring
    num_breeding_rabbits = 10
    num_kittens_first_spring = num_breeding_rabbits * 10
    num_kittens_adopted = num_kittens_first_spring // 2
    num_kittens_returned = 5
    num_kittens_in_house = num_kittens_first_spring - num_kittens_adopted + num_kittens_returned

    # Calculate the number of rabbits in the second spring
    num_kittens_second_spring = 60
    num_kittens_adopted_second_spring = 4
    num_kittens_in_house_second_spring = num_kittens_second_spring - num_kittens_adopted_second_spring
    num_rabbits_second_spring = num_kittens_in_house_second_spring // 5

    # Calculate the total number rabbits in Lola's house
    num_rabbits_total = num_breeding_rabbits + num_rabbits_second_spring
    result = num_rabbits_total
    return result

print(solution())