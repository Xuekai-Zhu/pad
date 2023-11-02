def solution():
    # Calculate the total weight of the luggage they have
    total_luggage_weight = 6 * 5 * 50  # 6 people with 5 bags weighing 50 pounds each

    # Calculate the maximum number of bags at maximum weight that the plane can hold
    max_bags = (6000 - total_luggage_weight) // 50  # // operator gives integer division

    result = max_bags
    return result

print(solution())