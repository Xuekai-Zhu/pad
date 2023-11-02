def solution():
    # Calculate the price of the cheaper pair of shoes after the offer
    cheaper_price = 40 / 2  # second pair of shoes is half off

    # Calculate the total price before the extra discount
    total_price = cheaper_price + 60  # first pair is $40, second pair after offer is $60

    # Calculate the total price after the extra discount
    final_price = total_price * (3/4)  # extra discount of a fourth off the total amount

    result = final_price
    return result

print(solution())