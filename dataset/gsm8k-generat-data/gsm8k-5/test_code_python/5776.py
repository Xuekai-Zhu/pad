def solution():
    # Calculate the total number of applications needed
    total_applications = 16 // 2  # Tiffany needs to re-apply sunscreen every 2 hours for 16 hours

    # Calculate the total amount of sunscreen needed
    total_sunscreen = total_applications * 3  # Tiffany needs 3 ounces of sunscreen for each application

    # Calculate the number of sunscreen bottles needed
    total_bottles = total_sunscreen / 12  # Each sunscreen bottle contains 12 ounces

    # Calculate the total cost of the sunscreen
    total_cost = total_bottles * 3.5  # Each sunscreen bottle costs $3.5

    result = total_cost
    return result

print(solution())