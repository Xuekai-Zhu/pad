def solution():
    cola_price = 3.0
    juice_price = 1.5
    water_price = 1.0

    num_cola_bottles = 15
    num_juice_bottles = 12
    num_water_bottles = 25

    # Calculate the total earnings from cola
    cola_earnings = num_cola_bottles * cola_price

    # Calculate the total earnings from juice
    juice_earnings = num_juice_bottles * juice_price

    # Calculate the total earnings from water
    water_earnings = num_water_bottles * water_price

    # Calculate the total earnings from all the bottled drinks
    total_earnings = cola_earnings + juice_earnings + water_earnings
    result = total_earnings
    return result

print(solution())