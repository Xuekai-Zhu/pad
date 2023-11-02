def solution():
    sports_arena_capacity = 16740
    coachella_attendance = 99000
    if coachella_attendance > sports_arena_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())