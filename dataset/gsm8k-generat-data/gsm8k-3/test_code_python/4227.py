def solution():
  """A community is building a metal fence. Each fence panel is made of 3 metal sheets, and 2 metal beams. The fence is made of 10 fence panels. If each sheet is made of 10 metal rods and each metal beam is made of 4 metal rods, how many metal rods does the community need for the fence?"""
  # Define the number of metal rods in each sheet and beam
  RODS_PER_SHEET = 10
  RODS_PER_BEAM = 4

  # Calculate the total number of metal rods needed for the fence
  rods_per_panel = 3 * RODS_PER_SHEET + 2 * RODS_PER_BEAM
  total_rods = rods_per_panel * 10

  # Display the total number of metal rods needed
  result = total_rods
  return result

print(solution())