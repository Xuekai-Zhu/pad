def solution():
    # Calculate the number of corn ears Marcel bought
    marcel_corn = 10

    # Calculate the number of corn ears Dale bought
    dale_corn = marcel_corn / 2

    # Calculate the total number of potatoes bought
    total_potatoes = 8 + marcel_potatoes

    # Calculate the total number of vegetables bought
    total_veggies = marcel_corn + dale_corn + total_potatoes

    # Solve for the number of potatoes Marcel bought
    marcel_potatoes = (total_veggies - 27) / 2

    result = marcel_potatoes
    return result

print(solution())