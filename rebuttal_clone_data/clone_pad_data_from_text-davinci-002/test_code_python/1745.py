def solution():
     rate_mila = 10
     rate_agnes = 15
     hours_agnes = 8
     hours_mila = (hours_agnes * 4) * (rate_agnes / rate_mila)
     result = hours_mila
     return result

print(solution())