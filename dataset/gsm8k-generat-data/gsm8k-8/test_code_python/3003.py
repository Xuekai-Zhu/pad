def solution():
  # Define the depth of the river in mid-July
  depth_july = 45

  # Calculate the depth of the river in mid-June
  depth_june = depth_july / 3

  # Calculate the depth of the river in mid-May
  depth_may = depth_june - 10

  result = depth_may
  return result

print(solution())