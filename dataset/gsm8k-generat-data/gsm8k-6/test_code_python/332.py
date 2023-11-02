def solution():
    # Calculate the amount of taxes Dorothy needs to pay
    taxes = 0.18 * 60000

    # Calculate the amount of money Dorothy will have left
    money_left = 60000 - taxes
    result = money_left
    return result

print(solution())