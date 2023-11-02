def solution():
    # Calculate the total number of days Olaf needs to travel to cover 4,000 miles
    total_days = 4000/200

    # Calculate the total amount of water Olaf needs for the journey
    total_water = (1/2) * 25 * total_days  # 25 men, including Olaf, and 1/2 a gallon of water per day per man
    result = total_water
    return result

print(solution())