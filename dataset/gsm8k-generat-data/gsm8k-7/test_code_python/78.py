def solution():
    num_cookie_pies = 3
    slices_per_pie = 10
    num_people = 24 + 1 # 24 classmates and 1 teacher
    num_slices_eaten = num_people * num_cookie_pies
    num_slices_left = (num_cookie_pies * slices_per_pie) - num_slices_eaten
    result = num_slices_left
    return result

print(solution())