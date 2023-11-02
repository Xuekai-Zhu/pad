def solution():
     miles_run_by_Billy = [1, 1, 1, 1, 1, 1]
     miles_run_by_Tiffany = [2, 2, 2, 1/3, 1/3, 1/3]
     total_miles_run_by_Billy = sum(miles_run_by_Billy)
     total_miles_run_by_Tiffany = sum(miles_run_by_Tiffany)
     needed_miles_by_Billy = total_miles_run_by_Tiffany - total_miles_run_by_Billy
     result = needed_miles_by_Billy
     return result

print(solution())