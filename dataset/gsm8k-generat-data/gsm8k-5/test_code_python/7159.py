def solution():
    jalen_weight = 160  # Jalen weighs 160 pounds
    ponce_weight = jalen_weight - 10  # Ponce weighs 10 pounds less than Jalen
    ishmael_weight = ponce_weight + 20  # Ishmael weighs 20 pounds more than Ponce

    # Calculate the average weight of the three
    average_weight = (jalen_weight + ponce_weight + ishmael_weight) / 3
    result = average_weight
    return result

print(solution())