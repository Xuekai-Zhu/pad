def solution():
    num_male_orchestra = 11
    num_female_orchestra = 12
    num_male_band = num_male_orchestra * 2
    num_female_band = num_female_orchestra * 2
    num_male_choir = 12
    num_female_choir = 17

    # Calculate the total number of musicians in the orchestra
    total_orchestra = num_male_orchestra + num_female_orchestra

    # Calculate the total number of musicians in the band
    total_band = num_male_band + num_female_band

    # Calculate the total number of musicians in the choir
    total_choir = num_male_choir + num_female_choir

    # Calculate the total number of musicians
    total_musicians = total_orchestra + total_band + total_choir
    result = total_musicians
    return result

print(solution())