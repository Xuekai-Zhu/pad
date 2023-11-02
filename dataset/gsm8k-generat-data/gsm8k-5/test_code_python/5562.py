def solution():
    marcel_corn = 10  # Marcel buys 10 ears of corn
    dale_corn = marcel_corn / 2  # Dale buys half of that amount
    total_corn = marcel_corn + dale_corn  # The total number of ears of corn they bought
    total_veggies = 27  # They bought 27 vegetables in total
    dale_potatoes = 8  # Dale bought 8 potatoes
    marcel_potatoes = total_veggies - total_corn - dale_potatoes  # Marcel bought the remaining vegetables

    result = marcel_potatoes
    return result

print(solution())