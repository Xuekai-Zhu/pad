def solution():
    num_short_dresses = 5
    short_dress_price = 20

    num_pants = 3
    pants_price = 12

    num_jackets = 4
    jacket_price = 30

    transportation_cost = 5

    initial_money = 400

    # Calculate the total cost of all short dresses
    total_short_dress_cost = num_short_dresses * short_dress_price

    # Calculate the total cost of all pants
    total_pants_cost = num_pants * pants_price

    # Calculate the total cost of all jackets
    total_jacket_cost = num_jackets * jacket_price

    # Calculate the total cost of all items and transportation
    total_cost = total_short_dress_cost + total_pants_cost + total_jacket_cost + transportation_cost

    # Calculate how much money Rita has left
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())