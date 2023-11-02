def solution():
    
    initial_capacity = 350000
    loss_rate1 = 32000
    loss_rate2 = 10000
    fill_rate = 40000
    time1 = 5
    time2 = 10
    time3 = 3
    loss1 = loss_rate1 * time1
    loss2 = loss_rate2 * time2
    fill = fill_rate * time3
    total_loss = loss1 + loss2
    net_loss = total_loss - fill
    remaining_capacity = initial_capacity - net_loss
    missing_capacity = initial_capacity - remaining_capacity
    result = missing_capacity

    return result

print(solution())