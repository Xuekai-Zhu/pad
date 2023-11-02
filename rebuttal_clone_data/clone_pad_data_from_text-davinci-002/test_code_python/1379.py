def solution():
    breeding_rabbits_year_one = 10
    kittens_year_one = breeding_rabbits_year_one * 10
    kittens_adopted_year_one = kittens_year_one / 2
    kittens_returned_year_one = 5
    breeding_rabbits_year_two = 10
    kittens_year_two = 60
    kittens_adopted_year_two = 4
    total_rabbits = breeding_rabbits_year_one + kittens_year_one + breeding_rabbits_year_two + kittens_year_two - kittens_adopted_year_one - kittens_adopted_year_two + kittens_returned_year_one
    result = total_rabbits
    return result

print(solution())