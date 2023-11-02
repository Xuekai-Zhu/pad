def solution():
    # Calculate the initial amount of vegetables James eats per day
    initial_veggies = 0.25 + 0.25  # a quarter pound of asparagus and a quarter pound of broccoli

    # Calculate the amount of vegetables James eats per week after doubling and adding kale
    doubled_veggies = 2 * initial_veggies  # double the initial amount
    kale_per_week = 3  # 3 pounds of kale per week
    total_veggies = doubled_veggies * 7 + kale_per_week  # total amount of vegetables eaten per week

    result = total_veggies
    return result

print(solution())