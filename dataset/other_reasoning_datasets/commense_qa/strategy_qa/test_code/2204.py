def solution():
    # Define the average high and low temperatures in Hollywood in July
    high_temp = 77.2
    low_temp = 61.5
    # Check if the temperature is warm enough to not require a coat
    if low_temp >= 60 and high_temp <= 80:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())