def solution():
     money_given= 320
     cost_per_book= 12
     number_of_students= 30
     
     total_cost= cost_per_book*number_of_students
     if total_cost>money_given:
         result= total_cost-money_given
         
     else:
         result = 0
         
     return result

print(solution())