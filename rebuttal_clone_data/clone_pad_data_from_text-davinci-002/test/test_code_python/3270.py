def solution():
    minutes_in_an_hour = 60
    minutes_in_two_hours = minutes_in_an_hour * 2
    minutes_in_sixteen_hours = minutes_in_an_hour * 16
    number_of_applications = minutes_in_sixteen_hours / minutes_in_two_hours
    ounces_per_application = 3
    ounces_in_a_bottle = 12
    bottles_needed = number_of_applications * ounces_per_application / ounces_in_a_bottle
    cost_per_bottle = 3.5
    total_cost = cost_per_bottle * bottles_needed
    result = total_cost
    return result

print(solution())