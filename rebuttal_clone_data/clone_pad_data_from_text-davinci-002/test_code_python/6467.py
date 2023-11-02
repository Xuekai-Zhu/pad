def solution():
    new_york_temp = 80
    miami_temp = new_york_temp + 10
    san_diego_temp = miami_temp - 25
    average_temp = (new_york_temp + miami_temp + san_diego_temp) / 3
    result = average_temp
    return result

print(solution())