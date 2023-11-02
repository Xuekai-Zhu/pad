def solution():
    # Let's assume Jason had x amount of money at first.
    # Calculate how much money he had left after buying books
    remaining_money_after_books = (3/4)*x - 10

    # Calculate how much money he had left after buying DVDs
    remaining_money_after_DVDs = (3/5)*remaining_money_after_books - 8

    # Set this remaining money equal to $130 and solve for x
    x = (remaining_money_after_DVDs + 130) * (5/3)
    result = x
    return result

print(solution())