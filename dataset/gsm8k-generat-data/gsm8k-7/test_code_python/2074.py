def solution():
    num_guests = 12
    participant_contribution = 5
    samanta_contribution = 10
    leftover_money = 15

    # Calculate the total amount of money collected
    total_money_collected = (num_guests * participant_contribution) + samanta_contribution

    # Calculate the actual cost of the gift
    actual_gift_cost = total_money_collected - leftover_money

    # Calculate the price of the gift per guest
    price_per_guest = actual_gift_cost / num_guests
    result = price_per_guest
    return result

print(solution())