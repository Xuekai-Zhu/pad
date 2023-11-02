def solution():
    num_students = 25  # There are 25 students in the class
    num_vampire_bags = 11  # 11 students want vampire-themed bags
    num_pumpkin_bags = 14  # 14 students want pumpkin-themed bags

    # Calculate the number of packages needed for each theme
    num_vampire_packages = (num_vampire_bags + 4) // 5  # Round up to the nearest package
    num_pumpkin_packages = (num_pumpkin_bags + 4) // 5  # Round up to the nearest package

    # Calculate the number of individual bags needed for each theme
    num_vampire_individual = num_vampire_bags % 5
    num_pumpkin_individual = num_pumpkin_bags % 5

    # Calculate the total cost for each theme
    vampire_cost = (num_vampire_packages * 3) + (num_vampire_individual * 1)
    pumpkin_cost = (num_pumpkin_packages * 3) + (num_pumpkin_individual * 1)

    # Calculate the least amount of money spent by the teacher
    total_cost = min(vampire_cost, pumpkin_cost)
    result = total_cost
    return result

print(solution())