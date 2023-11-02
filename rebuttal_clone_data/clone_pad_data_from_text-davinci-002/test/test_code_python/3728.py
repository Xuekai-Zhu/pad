def solution():
     number_of_boys = 300
     percent_of_girls = 60
     number_of_girls = (percent_of_girls / 100) * (number_of_boys / (1 - (percent_of_girls / 100)))
     result = number_of_girls
     return result

print(solution())