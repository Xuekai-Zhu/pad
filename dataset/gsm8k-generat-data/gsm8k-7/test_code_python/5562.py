def solution():
    marcel_corn = 10
    dale_corn = marcel_corn / 2
    dale_potatoes = 8
    total_veggies = 27

    # Calculate the number of potatoes Marcel bought
    marcel_potatoes = total_veggies - marcel_corn - dale_corn - dale_potatoes
    result = marcel_potatoes
    return result

print(solution())