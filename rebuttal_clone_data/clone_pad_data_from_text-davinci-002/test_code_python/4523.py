def solution():
     people_abducted = 200
     people_returned = people_abducted * 0.8
     people_taken_to_another_planet = 10
     people_taken_to_home_planet = people_abducted - people_returned - people_taken_to_another_planet
     result = people_taken_to_home_planet
     return result

print(solution())