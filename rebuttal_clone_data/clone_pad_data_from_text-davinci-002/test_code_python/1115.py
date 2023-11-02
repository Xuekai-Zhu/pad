def solution():
     scallops_per_pound = 8
     cost_per_pound = 24.00
     number_of_scallops = 2
     number_of_people = 8
     cost_of_scallops = scallops_per_pound * cost_per_pound * number_of_scallops / number_of_people
     result = cost_of_scallops
     return result

print(solution())