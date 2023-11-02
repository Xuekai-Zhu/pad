def solution():
    bike_cost = 2345
    saved_money = 1500
    lawns_mowed = 20
    newspapers_delivered = 600
    dogs_walked = 24
    lawn_payment = 20
    newspaper_payment = 0.4
    dog_payment = 15
    total_payment = (lawns_mowed * lawn_payment) + (newspapers_delivered * newspaper_payment) + (dogs_walked * dog_payment)
    money_left = saved_money + total_payment - bike_cost
    
    return money_left

print(solution())