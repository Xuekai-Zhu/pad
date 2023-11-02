def solution():
    # Calculate the total amount raised by the guests
    total_guest_money = 12 * 5

    # Calculate the total amount contributed by Samanta
    total_samanta_money = 10

    # Calculate the total amount available for the gift
    total_gift_money = total_guest_money + total_samanta_money - 15

    # Calculate the price of the gift
    gift_price = total_gift_money / 12

    result = gift_price
    return result

print(solution())