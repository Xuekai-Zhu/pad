def solution():
    soap_per_cup = 3  # The recipe calls for 3 tablespoons of soap for every 1 cup of water
    water_capacity = 40  # The container can hold 40 ounces of liquid
    water_per_cup = 8  # There are 8 ounces in a cup of water

    # Calculate the total water needed
    total_water = water_capacity / water_per_cup

    # Calculate the total soap needed
    total_soap = total_water * soap_per_cup

    result = total_soap
    return result

print(solution())