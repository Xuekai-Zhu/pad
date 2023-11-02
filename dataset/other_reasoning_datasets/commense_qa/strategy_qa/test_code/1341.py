def solution():
    mercury_used_in_thermometers = True
    thermometers_used_in_taking_body_temperature = True
    high_temperature_a_symptom_of_coronavirus = True
    if mercury_used_in_thermometers and thermometers_used_in_taking_body_temperature and high_temperature_a_symptom_of_coronavirus:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())