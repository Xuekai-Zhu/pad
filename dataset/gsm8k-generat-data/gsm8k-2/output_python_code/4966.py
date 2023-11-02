def solution():
    """A company has a tank that is already filled at a maximum capacity of 350,000 gallons of water. One day the tank starts losing 32,000 gallons/hour for 5 hours, after that time the company repaired the tank but it wasn't enough because the tank was still losing 10,000 gallons/hour. It stayed like that for 10 hours. In the second attempt, they managed to repair the tank and started filling it with 40,000 gallons/hour. After 3 hours, how many gallons are missing for the tank to be at maximum capacity again?"""
    tank_capacity = 350000
    first_loss_hours = 5
    first_loss_rate = 32000
    first_loss = first_loss_hours * first_loss_rate
    first_repair_loss_hours = 10
    first_repair_loss_rate = 10000
    first_repair_loss = first_repair_loss_hours * first_repair_loss_rate
    second_repair_rate = 40000
    second_repair_hours = 3
    second_repair = second_repair_rate * second_repair_hours
    total_loss = first_loss + first_repair_loss + second_repair
    remaining_capacity = tank_capacity - total_loss
    result = remaining_capacity
    return result

print(solution())