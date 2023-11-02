def solution():
    march_saving = 27
    april_saving = 13
    may_saving = 28
    keyboard_cost = 49
    mouse_cost = 5
    total_spent = keyboard_cost + mouse_cost
    total_saved = march_saving + april_saving + may_saving
    final_total = total_saved - total_spent
    result = final_total

    return result

print(solution())