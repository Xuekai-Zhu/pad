def solution():
     feet_of_rope_last_week = 6
     feet_of_rope_this_week = feet_of_rope_last_week - 4
     inches_in_a_foot = 12
     inches_of_rope_last_week = feet_of_rope_last_week * inches_in_a_foot
     inches_of_rope_this_week = feet_of_rope_this_week * inches_in_a_foot
     total_inches_of_rope = inches_of_rope_last_week + inches_of_rope_this_week
     result = total_inches_of_rope
     return result

print(solution())