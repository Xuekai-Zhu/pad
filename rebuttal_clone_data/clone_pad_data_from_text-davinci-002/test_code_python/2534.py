def solution():
    number_of_pies = 2
    slices_per_pie = 8
    slices_eaten = 2
    percent_eaten = 50
    number_of_slices_eaten = number_of_pies * slices_per_pie * (percent_eaten / 100)
    final_slices_eaten = slices_eaten + 2
    slices_remaining = number_of_pies * slices_per_pie - final_slices_eaten
    result = slices_remaining
    return result

print(solution())