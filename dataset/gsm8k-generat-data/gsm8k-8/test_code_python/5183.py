def solution():
  # Calculate the length of Miss Aisha's legs
  leg_length = 1/3 * 60

  # Calculate the length of Miss Aisha's head
  head_length = 1/4 * 60

  # Calculate the total length of Miss Aisha's legs and head
  leg_head_length = leg_length + head_length

  # Calculate the length of the rest of Miss Aisha's body
  body_length = 60 - leg_head_length

  result = body_length
  return result

print(solution())