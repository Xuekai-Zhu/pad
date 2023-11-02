def solution():
    total_eggs = 800
    percent_loss_1 = 10
    percent_loss_2 = 70
    percent_loss_1_actual = total_eggs * (percent_loss_1 / 100)
    percent_loss_2_actual = total_eggs * (percent_loss_2 / 100)
    total_loss = percent_loss_1_actual + percent_loss_2_actual
    remaining_eggs = total_eggs - total_loss
    percentage_hatched = 25
    actual_hatched = remaining_eggs * (percentage_hatched / 100)
    result = actual_hatched
    return result

print(solution())