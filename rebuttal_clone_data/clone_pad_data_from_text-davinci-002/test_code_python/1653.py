def solution():
     chapters = 8
     chapters_read = 2
     hours_taken = 3
     chapters_remaining = chapters - chapters_read
     hours_remaining = chapters_remaining / 2
     result = hours_taken + hours_remaining
     return result

print(solution())