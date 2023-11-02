def solution():
     students_who_like_blue = 200 * (30 / 100)
     students_who_like_red = 200 * (40 / 100)
     students_who_like_yellow = 200 - students_who_like_blue - students_who_like_red
     result = students_who_like_yellow + students_who_like_blue
     return result

print(solution())