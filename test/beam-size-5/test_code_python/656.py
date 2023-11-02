def solution():
    # Calculate the number of sheep on Lee's farm
    legs_on_farm = 70
    legs_on_farm = legs_on_farm * 2
    heads_on_farm = 20
    sheep_on_farm = legs_on_farm - legs_on_farm - heads_on_farm
    result = sheep_on_farm
    return result

print(solution())