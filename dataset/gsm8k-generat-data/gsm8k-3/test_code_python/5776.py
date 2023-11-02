def solution():
    """Tiffany is going to the beach and wants to make sure she has enough sunscreen. She knows she needs to re-apply sunscreen after 2 hours. She also knows she needs 3 ounces of sunscreen each application and a bottle contain 12 ounces and costs $3.5. If she is there for 16 hours, how much will the sunscreen cost?"""
    # Define the amount of sunscreen needed per application
    SUNSCREEN_PER_APPLICATION = 3

    # Define the size and cost of a bottle of sunscreen
    SUNSCREEN_SIZE = 12
    SUNSCREEN_COST = 3.5

    # Calculate the number of applications needed
    num_applications = 16 // 2  # integer division

    # Calculate the number of bottles needed
    num_bottles = (num_applications * SUNSCREEN_PER_APPLICATION) / SUNSCREEN_SIZE
    num_bottles = int(num_bottles) + 1 if num_bottles % 1 != 0 else int(num_bottles)

    # Calculate the total cost of the sunscreen
    total_cost = num_bottles * SUNSCREEN_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())