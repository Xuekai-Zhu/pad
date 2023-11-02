def solution():
 Christina_rate = 30
 friend_rate = 40
 total_distance = 210
 friend_time = 3
 Christina_time = (total_distance - (friend_rate * friend_time)) / Christina_rate
 result = Christina_time * 60
 return result

print(solution())