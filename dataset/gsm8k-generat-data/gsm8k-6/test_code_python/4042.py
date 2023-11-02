def solution():
    # Calculate the total cost of the land bought
    total_cost = 8000 + 4000

    # Calculate the size of the land bought
    size_of_land_bought = total_cost / 20  # land price is $20 per square meter

    # Calculate the total size of the land after buying new land
    total_size_of_land = 300 + size_of_land_bought

    result = total_size_of_land
    return result

print(solution())