def solution():
    jar_size = 10  # Tanya makes enough to fill a 10-ounce jar each time
    citrus_zest = 2 * jar_size  # Tanya uses the same amount of citrus zest as fragrance
    sugar = 2 * jar_size  # Tanya uses twice as much salt as zest
    oil = 2 * jar_size  # Tanya uses twice as much oil as salt

    # Calculate the total amount of oil Tanya uses
    total_oil = jar_size + citrus_zest + sugar + oil
    result = total_oil
    return result

print(solution())