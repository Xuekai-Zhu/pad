def solution():
     """Manny had 3 birthday cookie pies to share with his 24 classmates and his teacher, Mr. Keith. If each of the cookie pies were cut into 10 slices and Manny, his classmates, and Mr. Keith all had 1 piece, how many slices are left?"""
    cookie_pies = 3
    classmates = 24
    Mr_Keith = 1
    total_people = classmates + Mr_Keith
    slices_per_pie = 10
    total_slices = cookie_pies * slices_per_pie
    slices_left = total_slices - total_people
    result = slices_left
    return result

print(solution())