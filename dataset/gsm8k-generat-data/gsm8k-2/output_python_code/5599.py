def solution():
   """Charles is moving from Springfield, which has 482,653 people, to Greenville, which has 119,666 fewer people. What is the total population of Springfield and Greenville?"""
   springfield_population = 482653
   greenville_population = springfield_population - 119666
   total_population = springfield_population + greenville_population
   result = total_population
   return result

print(solution())