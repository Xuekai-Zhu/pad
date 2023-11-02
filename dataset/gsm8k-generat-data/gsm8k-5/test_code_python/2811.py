def solution():
    total_baby_mice = 3 * 8  # Brenda had 3 litters of 8 baby mice each
    given_away = total_baby_mice / 6  # Brenda gave away one sixth of the baby mice
    remaining = total_baby_mice - given_away  # Brenda has the remaining baby mice
    sold_to_store = given_away * 3  # Brenda sold three times the number of babies she gave Robbie to the pet store
    remaining -= sold_to_store  # Subtract the sold mice from the remaining to get mice not sold

    # Half of the remaining mice were sold to snake owners as feeder mice
    remaining /= 2
    result = remaining
    return result

print(solution())