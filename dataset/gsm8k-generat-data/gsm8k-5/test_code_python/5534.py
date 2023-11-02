def solution():
    mountain_bike_cost = 2345   # Cost of the mountain bike Julie wants to give
    money_saved = 1500          # Amount of money Julie has already saved
    lawns_mowed = 20            # Number of lawns Julie will mow for extra money
    newspapers_delivered = 600  # Number of newspapers Julie will deliver for extra money
    dogs_walked = 24            # Number of dogs Julie will walk for extra money
    lawn_payment = 20           # Amount paid for each lawn
    newspaper_payment = 0.40    # Amount paid for each newspaper
    dog_payment = 15            # Amount paid for each dog

    # Calculate the total amount of money Julie will earn
    total_earnings = (lawns_mowed * lawn_payment) + (newspapers_delivered * newspaper_payment) + (dogs_walked * dog_payment)

    # Calculate how much money Julie will have left after purchasing the mountain bike
    remaining_money = (money_saved + total_earnings) - mountain_bike_cost
    result = remaining_money
    return result

print(solution())