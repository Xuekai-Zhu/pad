def solution():
     bell_peppers = 5
     large_slices = 20
     small_slices = large_slices / 2
     small_pieces = small_slices * 3
     total_slices = large_slices + small_slices
     total_pieces = small_pieces + small_slices
 
     result = "Total slices: " + str(total_slices) + ". Total pieces: " + str(total_pieces)
     return result

print(solution())