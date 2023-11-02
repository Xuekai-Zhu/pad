def solution():
    target_price = 2345
    current_savings = 1500

    num_lawns = 20
    lawn_pay = 20

    num_newspapers = 600
    newspaper_pay = 0.4

    num_dogs = 24
    dog_pay = 15

    # Calculate the total amount of additional money Julie will earn
    lawn_money = num_lawns * lawn_pay
    newspaper_money = num_newspapers * newspaper_pay
    dog_money = num_dogs * dog_pay
    additional_money = lawn_money + newspaper_money + dog_money

    # Calculate Julie's total savings after earning additional money
    total_savings = current_savings + additional_money

    # Calculate the amount of money Julie will have left after purchasing the bike
    leftover_money = total_savings - target_price
    result = leftover_money
    return result

print(solution())