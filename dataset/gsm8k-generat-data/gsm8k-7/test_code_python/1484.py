def solution():
    final_money = 15

    # Calculate the amount of money remaining after losing one-third
    remaining_money1 = final_money / (1 - 1/3)

    # Calculate the amount of money remaining after spending one-fourth
    remaining_money2 = remaining_money1 * (1 - 1/4)

    # Calculate the initial amount of money Lucy had
    initial_money = remaining_money2
    result = initial_money
    return result

print(solution())