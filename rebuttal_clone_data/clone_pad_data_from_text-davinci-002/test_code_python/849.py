def solution():
     total_balloons = 200
     balloons_blown_up_1 = total_balloons / 5
     balloons_blown_up_2 = 2 * balloons_blown_up_1
     balloons_remaining = total_balloons - (balloons_blown_up_1 + balloons_blown_up_2)
     result = balloons_remaining
     return result

print(solution())