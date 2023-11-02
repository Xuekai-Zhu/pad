def solution():
    """Carla's brush is 12 inches long. If Carmen's brush is 50% longer than Carla's brush, how long is Carmen's brush in centimeters? (There are 2.5 centimeters per inch.)"""
    carla_brush_length = 12
    carmen_brush_length = carla_brush_length * 1.5
    carmen_brush_length_cm = carmen_brush_length * 2.5
    result = carmen_brush_length_cm
    return result

print(solution())