def solution():
    base_price = 3  # Elise paid a base price of $3
    per_mile_price = 4  # Elise paid $4 for every mile she traveled
    total_price = 23  # Elise paid a total of $23

    # Calculate the distance Elise traveled to reach the hospital
    distance = (total_price - base_price) / per_mile_price
    result = distance
    return result

print(solution())