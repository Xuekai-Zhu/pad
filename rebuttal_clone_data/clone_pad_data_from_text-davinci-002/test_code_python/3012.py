def solution():
     number_of_friends = 8
     slices_per_friend = 2
     slices_per_cake = 6
     number_of_cakes = 4
     number_of_slices_eaten = 3
     total_slices = number_of_friends * slices_per_friend + number_of_slices_eaten
     result = total_slices % slices_per_cake
     return result

print(solution())