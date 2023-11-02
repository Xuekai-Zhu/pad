def solution():
    #define the ratio
    cara_ratio = 4
    janet_ratio = 5
    jerry_ratio = 6

    #define the total amount of money
    total_money = 75

    #define the loss
    loss = total_money * 0.2

    #calculate the amount of money each person has
    cara_money = total_money * (cara_ratio / (cara_ratio + janet_ratio + jerry_ratio))
    janet_money = total_money * (janet_ratio / (cara_ratio + janet_ratio + jerry_ratio))
    jerry_money = total_money * (jerry_ratio / (cara_ratio + janet_ratio + jerry_ratio))

    #calculate the total loss
    total_loss = (cara_money + janet_money) * loss

    result = total_loss
    return result

print(solution())