def solution():
    car_cost = 2100  # The cost of the car is $2,100
    sister_days = 4  # Sue's sister will drive the car 4 days a week
    sue_days = 7 - sister_days  # Sue will drive the car for the remaining days

    # Calculate the percentage of use for Sue and her sister
    sister_percent = sister_days / 7
    sue_percent = sue_days / 7

    # Calculate how much each has to pay based on percentage of use
    sister_payment = car_cost * sister_percent
    sue_payment = car_cost * sue_percent

    # Calculate how much Sue has to pay
    total_payment = sister_payment + sue_payment
    sue_share = sue_payment
    result = sue_share
    return result

print(solution())