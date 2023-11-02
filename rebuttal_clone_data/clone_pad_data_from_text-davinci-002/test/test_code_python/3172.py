def solution():
     lines_of_code = 4300
     lines_between_debugs = 100
     errors_per_debug = 3
     total_errors_fixed = (lines_of_code // lines_between_debugs) * errors_per_debug
     result = total_errors_fixed
     return result

print(solution())