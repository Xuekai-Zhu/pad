def solution():
    julie_cost = 10
    letitia_cost = 20
    anton_cost = 30
    tip_percentage = 0.20
    total_cost = julie_cost + letitia_cost + anton_cost

    # Calculate the total tip amount
    total_tip = total_cost * tip_percentage

    # Calculate the amount each person should pay in tips
    num_people = 3
    tip_per_person = total_tip / num_people
    result = tip_per_person
    return result

print(solution())