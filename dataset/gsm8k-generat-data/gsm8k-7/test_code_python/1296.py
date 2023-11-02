def solution():
    num_carpets_house1 = 12
    num_carpets_house2 = 20
    num_carpets_house3 = 10
    num_carpets_house4 = num_carpets_house3 * 2

    # Calculate the total number of carpets across all houses
    total_carpets = num_carpets_house1 + num_carpets_house2 + num_carpets_house3 + num_carpets_house4
    result = total_carpets
    return result

print(solution())