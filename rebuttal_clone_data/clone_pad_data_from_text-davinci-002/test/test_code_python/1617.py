def solution():
  time_to_home = 10
  time_to_airport = time_to_home * 5
  time_to_check_bag = 15
  time_to_security = time_to_check_bag * 3
  time_to_board = 20
  time_to_takeoff = time_to_board * 2
  total_time = time_to_home + time_to_airport + time_to_check_bag + time_to_security + time_to_board + time_to_takeoff
  result = total_time / 60
  return result

print(solution())