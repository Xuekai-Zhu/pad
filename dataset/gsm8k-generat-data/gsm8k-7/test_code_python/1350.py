def solution():
    num_jars = 4
    num_caterpillars_per_jar = 10
    conversion_rate = 0.6  # 40% fail to become butterflies, so 60% become butterflies
    butterfly_price = 3.0

    # Calculate the total number of caterpillars that John has
    total_caterpillars = num_jars * num_caterpillars_per_jar

    # Calculate the number of butterflies that John will have
    num_butterflies = int(total_caterpillars * conversion_rate)

    # Calculate the total money that John will make from selling the butterflies
    total_money = num_butterflies * butterfly_price
    result = total_money
    return result

print(solution())