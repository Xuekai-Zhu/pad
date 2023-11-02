def solution():
     apples_needed_per_pie = 1.5 * 8
     apples_needed_total = apples_needed_per_pie * 3
     guests = 12
     apples_eaten_per_guest = apples_needed_total / guests
     result = apples_eaten_per_guest
     return result

print(solution())