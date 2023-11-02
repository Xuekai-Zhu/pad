def solution():
    # Calculate the cost for walking one dog for 10 minutes
    cost_dog_1 = 20 + (1 * 10)

    # Calculate the cost for walking two dogs for 7 minutes
    cost_dog_2 = (2 * 20) + (2 * 7)

    # Calculate the cost for walking three dogs for 9 minutes
    cost_dog_3 = (3 * 20) + (3 * 9)

    # Calculate the total earnings
    total_earnings = cost_dog_1 + cost_dog_2 + cost_dog_3
    result = total_earnings
    return result

print(solution())