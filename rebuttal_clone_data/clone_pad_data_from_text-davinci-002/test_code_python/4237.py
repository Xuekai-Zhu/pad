def solution():
    total_race_length = 74.5
    first_part_length = 15.5
    second_and_third_part_length = 21.5
    fourth_part_length = total_race_length - (first_part_length + (second_and_third_part_length * 2))
    result = fourth_part_length
  
    return result

print(solution())