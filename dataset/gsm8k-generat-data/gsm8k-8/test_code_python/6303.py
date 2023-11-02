def solution():
  # Calculate the minimum number of dark blue marbles
  min_db_marbles = 63 / 3

  # Calculate the sum of dark blue and green marbles
  db_green_sum = min_db_marbles + 4

  # Calculate the number of red marbles
  red_marbles = 63 - db_green_sum

  # Return the result
  return red_marbles

print(solution())