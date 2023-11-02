def solution():
    """A spaceship is traveling to another planet. The spaceship travels at a consistent speed its entire journey unless it is stopped for the crew’s break. After launch, the spaceship traveled for 10 hours then stopped for 3 hours. It then traveled for another 10 hours then stopped for 1 hour. After this, the spaceship would take an hour’s break after every 11 hours of traveling and maintained this routine until the end of its journey. If the entire journey took 3 days then how long, in hours, was the spaceship not moving?"""
    total_hours_in_3_days = 72
    travel_hours_before_first_break = 10 + 3 + 10 + 1
    travel_hours_per_cycle = 11
    break_hours_per_cycle = 1
    total_travel_hours = total_hours_in_3_days - travel_hours_before_first_break
    num_cycles = total_travel_hours // (travel_hours_per_cycle + break_hours_per_cycle)
    remaining_travel_hours = total_travel_hours - num_cycles * (travel_hours_per_cycle + break_hours_per_cycle)
    total_break_hours = num_cycles * break_hours_per_cycle + 4  # include the first two breaks
    result = total_break_hours
    return result

print(solution())