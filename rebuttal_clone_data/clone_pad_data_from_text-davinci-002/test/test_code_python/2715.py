def solution():
     joseph_mph = 50
     joseph_hours = 2.5
     kyle_mph = 62
     kyle_hours = 2
     joseph_miles = joseph_mph * joseph_hours
     kyle_miles = kyle_mph * kyle_hours
     difference = abs(joseph_miles - kyle_miles)
     result = difference
     return result

print(solution())