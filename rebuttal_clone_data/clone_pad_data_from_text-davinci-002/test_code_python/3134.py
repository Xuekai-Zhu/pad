def solution():
    total_steps_goal = 9000
    steps_ taken_so_far = 9400 + 9100 + 8300 + 9200 + 8900
    steps_remaining = total_steps_goal * 2 - steps_taken_so_far
    result = steps_remaining / 2
    return result

print(solution())