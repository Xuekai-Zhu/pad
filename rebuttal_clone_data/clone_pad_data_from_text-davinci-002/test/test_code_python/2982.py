def solution():
     excellent_percent = 15
     very_satisfactory_percent = 60
     satisfactory_percent = 80
 
     excellent_count = excellent_percent * 120 / 100
     very_satisfactory_count = very_satisfactory_percent * 120 / 100
     satisfactory_count = satisfactory_percent * (120 - excellent_count - very_satisfactory_count) / 100
 
     needs_improvement_count = 120 - excellent_count - very_satisfactory_count - satisfactory_count
     result = needs_improvement_count
     return result

print(solution())