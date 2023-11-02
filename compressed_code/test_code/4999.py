def solution():
    
    NY_temp = 80
    Miami_temp = NY_temp + 10
    SD_temp = Miami_temp + 25
    avg_temp = (NY_temp + Miami_temp + SD_temp) / 3
    result = avg_temp
    return result

print(solution())