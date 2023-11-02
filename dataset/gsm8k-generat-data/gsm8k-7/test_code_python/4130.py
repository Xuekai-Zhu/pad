def solution():
    weight_increase = 60
    ratio = 3

    # Calculate the weight Kyle lifted last year
    last_year_weight = weight_increase / ratio

    # Calculate the total weight Kyle can lift
    total_weight = last_year_weight + weight_increase
    result = total_weight
    return result

print(solution())