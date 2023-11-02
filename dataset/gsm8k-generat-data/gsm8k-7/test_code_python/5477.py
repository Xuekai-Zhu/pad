def solution():
    num_cows = 20
    num_pigs = 4 * num_cows

    pig_price = 400
    cow_price = 800

    # Calculate the total amount of money from selling all pigs
    total_pig_money = num_pigs * pig_price

    # Calculate the total amount of money from selling all cows
    total_cow_money = num_cows * cow_price

    # Calculate the total amount of money from selling all animals
    total_money = total_pig_money + total_cow_money
    result = total_money
    return result

print(solution())