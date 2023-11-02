def solution():
    car_cost = 2100  # total cost of the car
    sister_days = 4  # number of days sister drives the car in a week
    sue_days = 7 - sister_days  # number of days Sue gets to use the car in a week
    sister_percent = sister_days / 7  # percentage of days sister uses the car
    sue_percent = 1 - sister_percent  # percentage of days Sue uses the car
    sue_share = sue_percent * car_cost  # amount Sue has to pay
    result = sue_share
    return result

print(solution())