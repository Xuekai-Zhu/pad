def solution():
     jars_of_quarters = 5
     quarters_per_jar = 160
     quarters_needed = 180
     quarters_leftover = jars_of_quarters * quarters_per_jar - quarters_needed
     dollars_leftover = quarters_leftover / 4
     result = dollars_leftover
     return result

print(solution())