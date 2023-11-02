def solution():
    starting_weight = 300
    first_month_loss = 20
    total_loss = first_month_loss
    month = 2

    while True:
        current_loss = 0.5 * first_month_loss
        total_loss += current_loss
        starting_weight -= current_loss

        if month == 5:
            fifth_month_loss = starting_weight - 250.5
            result = fifth_month_loss
            return result

        first_month_loss = current_loss
        month += 1

print(solution())