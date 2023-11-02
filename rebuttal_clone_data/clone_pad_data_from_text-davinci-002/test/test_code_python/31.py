def solution():
     
     total_kilos = 10
     butter_used = total_kilos / 2 + total_kilos / 5 + (total_kilos - ((total_kilos / 2) + (total_kilos / 5))) / 3
     butter_left = total_kilos - butter_used
     result = butter_left
     return result

print(solution())