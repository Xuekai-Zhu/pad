def solution():
    """Johnny's dad brought him to watch some horse racing and his dad bet money. On the first race, he lost $5. On the second race, he won $1 more than twice the amount he previously lost. On the third race, he lost 1.5 times as much as he won in the second race. How much did he lose on average that day?"""
    race_1_loss = 5
    race_2_win = (2 * race_1_loss) + 1
    race_3_loss = 1.5 * race_2_win
    total_loss = race_1_loss + race_2_win + race_3_loss
    average_loss = total_loss / 3
    result = average_loss
    return result

print(solution())