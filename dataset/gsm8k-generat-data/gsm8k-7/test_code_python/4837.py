def solution():
    high_heels_price = 60
    ballet_slippers_price = (2/3) * high_heels_price
    num_ballet_slippers = 5

    # Calculate the total cost of all high heels
    total_high_heels_cost = high_heels_price

    # Calculate the total cost of all ballet slippers
    total_ballet_slippers_cost = ballet_slippers_price * num_ballet_slippers

    # Calculate the total cost of all shoes
    total_cost = total_high_heels_cost + total_ballet_slippers_cost
    result = total_cost
    return result

print(solution())