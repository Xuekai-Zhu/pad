def solution():
    mail_carriers_work_weather_independent = True
    leave_vehicle_in_various_weather_conditions = True
    if mail_carriers_work_weather_independent and leave_vehicle_in_various_weather_conditions:
        need_multiple_uniforms = True
    else:
        need_multiple_uniforms = False
    if need_multiple_uniforms:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())