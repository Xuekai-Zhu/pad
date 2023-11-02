def solution():
    carla_brush_length = 12  # in inches
    carmen_brush_length = carla_brush_length * 1.5  # carmen's brush is 50% longer than carla's
    carmen_brush_length_cm = carmen_brush_length * 2.5  # 1 inch = 2.5 cm
    result = carmen_brush_length_cm
    return result

print(solution())