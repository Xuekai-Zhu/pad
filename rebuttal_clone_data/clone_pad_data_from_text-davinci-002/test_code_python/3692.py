def solution():
     class_one_males = 17
     class_one_females = 13
     class_two_males = 14
     class_two_females = 18
     class_three_males = 15
     class_three_females = 17
     total_males = class_one_males + class_two_males + class_three_males
     total_females = class_one_females + class_two_females + class_three_females
     if total_males == total_females:
         result = 0
     elif total_males < total_females:
         result = total_males - total_females
     else:
         result = total_females - total_males
     return result

print(solution())