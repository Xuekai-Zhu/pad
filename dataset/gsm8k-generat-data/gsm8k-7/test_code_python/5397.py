def solution():
    baseball_cards = 25
    baseball_bat = 10
    baseball_glove = 30
    glove_discount = 0.20  # 20% discount
    cleats = 10

    # Calculate the discount on the baseball glove
    glove_discount_amount = glove_discount * baseball_glove

    # Calculate the total amount Grant made from selling his baseball gear
    total_money = baseball_cards + baseball_bat + (baseball_glove - glove_discount_amount) + (2 * cleats)

    result = total_money
    return result

print(solution())