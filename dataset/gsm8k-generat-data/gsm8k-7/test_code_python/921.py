def solution():
    num_people = 90

    num_soda_cans = 50
    soda_consumption_rate = 0.5

    num_sparkling_water_bottles = 50
    sparkling_water_consumption_rate = 1/3

    num_juice_bottles = 50
    juice_consumption_rate = 4/5

    # Calculate the number of people who drank soda
    num_people_drinking_soda = num_people * soda_consumption_rate

    # Calculate the number of people who drank sparkling water
    num_people_drinking_sparkling_water = num_people * sparkling_water_consumption_rate

    # Calculate the number of people who drank juice
    num_people_drinking_juice = num_people * (1 - soda_consumption_rate - sparkling_water_consumption_rate)

    # Calculate the number of soda cans that were consumed
    num_soda_cans_consumed = num_people_drinking_soda * (num_soda_cans/num_people)

    # Calculate the number of plastic bottles of sparkling water that were consumed
    num_sparkling_water_bottles_consumed = num_people_drinking_sparkling_water * (num_sparkling_water_bottles/num_people)

    # Calculate the number of glass bottles of juice that were consumed
    num_juice_bottles_consumed = num_people_drinking_juice * (num_juice_bottles/num_people) * juice_consumption_rate

    # Calculate the total number of recyclable cans and bottles
    total_num_recyclable = num_soda_cans_consumed + num_sparkling_water_bottles_consumed + num_juice_bottles_consumed

    result = total_num_recyclable
    return result

print(solution())