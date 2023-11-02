def solution():
    # Calculate the total weight of the girls
    weight_girls = 5 * 45  # 5 girls with an average weight of 45 kg

    # Calculate the total weight of the boys
    weight_boys = 5 * 55  # 5 boys with an average weight of 55 kg

    # Calculate the total weight of all ten students
    total_weight = weight_girls + weight_boys

    # Calculate the average weight of all ten students
    avg_weight = total_weight / 10
    result = avg_weight
    return result

print(solution())