def solution():
    # Calculate the weights of Ponce and Ishmael based on Jalen's weight
    weight_Jalen = 160
    weight_Ponce = weight_Jalen - 10
    weight_Ishmael = weight_Ponce + 20

    # Find the average weight of the three
    average_weight = (weight_Jalen + weight_Ponce + weight_Ishmael) / 3
    result = average_weight
    return result

print(solution())