def solution():
    package_size = 200  # There are 200 grams of cheese in each package
    price_white = 5  # The price of one package of white cheese is $5
    price_swiss = 6  # The price of one package of swiss cheese is $6
    price_blue = 8  # The price of one package of blue cheese is $8

    # Calculate the amount of white cheese needed
    amount_white = (5 * package_size) * (2/3)  # Miley needs 5 packages of swiss cheese, so she needs 5 * (2/3) = 3 1/3 packages of white cheese
    packages_white = amount_white / package_size  # Each package contains 200 grams of cheese
    cost_white = packages_white * price_white  # The cost of the white cheese

    # Calculate the cost of the swiss cheese
    cost_swiss = 5 * price_swiss  # Miley needs 5 packs of swiss cheese, so the cost of swiss cheese is just 5 * $6 = $30

    # Calculate the cost of the blue cheese
    packages_blue = 600 / package_size  # Miley needs 600 grams of blue cheese
    cost_blue = packages_blue * price_blue  # The cost of the blue cheese

    # Calculate the total cost of all the cheese
    total_cost = cost_white + cost_swiss + cost_blue
    result = total_cost
    return result

print(solution())