def solution():
    milk_per_glass = 6.5
    syrup_per_glass = 1.5

    total_milk = 130
    total_syrup = 60

    # Calculate the maximum number of glasses of chocolate milk Charles can make
    max_glasses = min(total_milk // milk_per_glass, total_syrup // syrup_per_glass)

    # Calculate the total amount of chocolate milk Charles will drink
    total_milk_drunk = max_glasses * milk_per_glass
    total_syrup_drunk = max_glasses * syrup_per_glass
    total_chocolate_milk = total_milk_drunk + total_syrup_drunk
    result = total_chocolate_milk
    return result

print(solution())