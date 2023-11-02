def solution():
    porsche_top_speed = 62 # mph
    usain_bolt_top_speed = 27.79 # mph
    sprint_distance = 100 # meters
    # Convert Porsche's top speed from mph to meters/second
    porsche_speed_mps = porsche_top_speed * 0.447 # 1 mph = 0.447 m/s
    # Calculate the time it would take for Porsche to cover 100 meters
    porsche_time = sprint_distance / porsche_speed_mps
    # Calculate the time it would take for Usain Bolt to cover 100 meters
    bolt_time = sprint_distance / (usain_bolt_top_speed * 0.447)
    if porsche_time < bolt_time:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())