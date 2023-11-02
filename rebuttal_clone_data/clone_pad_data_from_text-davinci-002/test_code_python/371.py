def solution():
     hamburgers_per_grilling_session = 15
     total_hamburgers_needed = 115
     hamburgers_already_cooked = 40
     burgers_left_to_cook = total_hamburgers_needed - hamburgers_already_cooked
     grilling_sessions_needed = burgers_left_to_cook / hamburgers_per_grilling_session
     result = grilling_sessions_needed
     return result

print(solution())