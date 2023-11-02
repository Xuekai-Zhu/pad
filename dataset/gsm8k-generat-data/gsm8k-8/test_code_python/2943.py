def solution():
    # Define the initial temperature
    initial_temp = 40

    # Jerry doubles the temperature
    jerry_temp = initial_temp * 2

    # Jerry's dad reduces the temperature by 30 degrees
    dad_temp = jerry_temp - 30

    # Jerry's mom reduces the temperature by 30%
    mom_temp = dad_temp * 0.7

    # Jerry's sister increases the temperature by 24 degrees
    final_temp = mom_temp + 24
    result = final_temp
    return result

print(solution())