def solution():
    """Jason is planning a parking garage that will have 12 floors. Every 3rd floor has a gate where drivers have to show ID, which takes two minutes. To get from one floor to the next, drivers have to drive 800 feet at 10 feet/second. How long, in seconds, does it take to get to the bottom of the garage from the top?"""
    num_floors = 12
    gate_floors = range(3, num_floors + 1, 3)
    gate_time = 2 * len(gate_floors)
    drive_distance = 800 * (num_floors - len(gate_floors))
    drive_time = drive_distance / 10
    total_time = gate_time + drive_time
    result = total_time
    return result

print(solution())