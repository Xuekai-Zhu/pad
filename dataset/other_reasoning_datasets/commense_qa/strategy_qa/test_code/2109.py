def solution():
    battery_voltage = 202
    nickel_melting_point = 2651
    microwave_warming_temp = 212
    # Convert the melting point from Fahrenheit to Celsius
    nickel_melting_point_celsius = (nickel_melting_point - 32) * (5/9)
    if microwave_warming_temp < nickel_melting_point_celsius and battery_voltage < 1000:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())