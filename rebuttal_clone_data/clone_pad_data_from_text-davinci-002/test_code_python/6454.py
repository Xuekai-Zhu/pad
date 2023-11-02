def solution():
     original_group = 9
     new_group = original_group + ((3 * original_group) - 2)
     scared_group = new_group / 2
     remaining_group = new_group - scared_group
     result = remaining_group
     return result

print(solution())