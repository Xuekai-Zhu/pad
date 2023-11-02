def solution():
    hardware_material = "titanium"
    metal_detector_effect = "no"
    earth_magnetic_field_effect = "yes"
    if hardware_material == "titanium" and metal_detector_effect == "no" and earth_magnetic_field_effect == "yes":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())