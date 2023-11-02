def solution():
     original_length = 143
     length_after_first_cut = original_length - 25
     length_after_second_cut = length_after_first_cut - 7
     result = length_after_second_cut
     return result

print(solution())