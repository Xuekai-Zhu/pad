def solution():
     money_raised = 50
     money_contributed = 5
     number_of_students = 20
     cost_of_trip = 7
     money_left = money_raised + (money_contributed * number_of_students) - (cost_of_trip * number_of_students)
     result = money_left
     return result

print(solution())