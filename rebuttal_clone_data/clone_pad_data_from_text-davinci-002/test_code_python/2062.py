def solution():
     total_time = 2
     piano_time = 0.5
     computer_time = 0.42
     reading_time = 0.63
     finger_exerciser_time = total_time - (piano_time + computer_time + reading_time)
     result = finger_exerciser_time
     return result

print(solution())