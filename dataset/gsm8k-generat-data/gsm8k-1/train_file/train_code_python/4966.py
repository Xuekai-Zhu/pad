def solution():
    """A company has a tank that is already filled at a maximum capacity of 350,000 gallons of water. One day the tank starts losing 32,000 gallons/hour for 5 hours, after that time the company repaired the tank but it wasn't enough because the tank was still losing 10,000 gallons/hour. It stayed like that for 10 hours. In the second attempt, they managed to repair the tank and started filling it with 40,000 gallons/hour. After 3 hours, how many gallons are missing for the tank to be at maximum capacity again?"""
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