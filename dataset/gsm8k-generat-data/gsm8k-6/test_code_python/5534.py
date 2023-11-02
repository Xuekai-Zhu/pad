def solution():
    # Calculate how much money Julie will earn from mowing lawns
    lawns_money = 20 * 20  # Julie is paid $20 for each lawn

    # Calculate how much money Julie will earn from delivering newspapers
    newspaper_money = 0.4 * 600  # Julie is paid 40 cents per newspaper

    # Calculate how much money Julie will earn from walking dogs
    dog_money = 15 * 24  # Julie is paid $15 per dog

    # Add up all the money Julie will earn
    total_money = lawns_money + newspaper_money + dog_money

    # Calculate how much money Julie will have left after purchasing the mountain bike
    bike_cost = 2345
    money_left = total_money - bike_cost + 1500

    result = money_left
    return result

print(solution())