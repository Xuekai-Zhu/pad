def solution():
    """Tiffany is going to the beach and wants to make sure she has enough sunscreen. She knows she needs to re-apply sunscreen after 2 hours. She also knows she needs 3 ounces of sunscreen each application and a bottle contain 12 ounces and costs $3.5. If she is there for 16 hours, how much will the sunscreen cost?"""
    # Define the amount of sunscreen needed for each application and the size of each bottle
    sunscreen_per_application = 3
    bottle_size = 12

    # Calculate the number of applications needed for a 16-hour beach day
    num_applications = 16 // 2

    # Calculate the total amount of sunscreen needed
    total_sunscreen = num_applications * sunscreen_per_application

    # Calculate the number of bottles needed
    num_bottles = total_sunscreen // bottle_size + 1

    # Calculate the total cost of the sunscreen
    total_cost = num_bottles * 3.5

    result = total_cost
    return result

print(solution())