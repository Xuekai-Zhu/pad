def solution():
    kobe_order = 5  # Kobe ordered 5 pieces of fried chicken
    pau_order = kobe_order * 2  # Pau ordered twice as much fried chicken as Kobe
    total_order = kobe_order + pau_order  # They ordered a total of kobe_order + pau_order pieces of fried chicken
    total_eaten = total_order * 2  # They order another set, so they will eat twice as much as they ordered
    pau_eaten = total_eaten - kobe_order * 2  # Pau ate twice as much as Kobe in the first order, so he will eat twice as much in the second order too

    result = pau_eaten
    return result

print(solution())