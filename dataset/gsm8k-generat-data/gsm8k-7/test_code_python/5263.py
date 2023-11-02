def solution():
    car_cost = 2100
    sister_days = 4
    sue_days = 7 - sister_days

    # Calculate the percentage of car use for Sue
    sue_percentage = sue_days / 7

    # Calculate how much Sue needs to pay
    sue_payment = sue_percentage * car_cost
    result = sue_payment
    return result

print(solution())