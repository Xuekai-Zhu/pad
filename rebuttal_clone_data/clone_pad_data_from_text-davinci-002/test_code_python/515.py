def solution():
    temp = 8
    initial_chance = 0
    drop_in_temp = 32 - temp
    drop_in_temp_divided = drop_in_temp / 3
    increase_in_chance = drop_in_temp_divided * 5
    new_chance = initial_chance + increase_in_chance
    skidding_chance = new_chance / 100
    chance_of_recovering = 0.40
    chance_of_not_recovering = 1 - chance_of_recovering
    chance_of_accident = skidding_chance * chance_of_not_recovering
    result = chance_of_accident * 100
    return result

print(solution())