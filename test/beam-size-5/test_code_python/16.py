def solution():
    
    # Define the amount of water in the orange drink
    orange_drink = 10

    # Define the amount of water in the pineapple drink
    pineapple_drink = 15

    # Calculate the amount of water in the orange drink
    orange_drink_water = orange_drink * (2/3)

    # Calculate the amount of water in the pineapple drink
    pineapple_drink_water = pineapple_drink * (3/5)

    # Calculate the amount of water in the remaining 24 liters
    remaining_drink = 24 - orange_drink_water - pineapple_drink_water

    # Display the amount of water in the remaining 24 liters
    result = remaining_drink
    return result

print(solution())