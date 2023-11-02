def solution():
   butter_needed = 6 * 2
   butter_available = 4
   butter_used = min(butter_available, butter_needed)
   coconut_oil_used = butter_needed - butter_used
   result = coconut_oil_used
   return result

print(solution())