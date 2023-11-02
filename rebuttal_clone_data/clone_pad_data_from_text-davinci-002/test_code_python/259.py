def solution():
     """Adam goes to a small school, which teaches 80 students in three classes. 40% of the students are in class A, and class B has 21 students fewer than class A. The rest are in class C. How many students are in class C?"""
     total_students = 80
     percent_in_A = 40
     num_in_A = total_students * (percent_in_A / 100)
     num_in_B = num_in_A - 21
     num_in_C = total_students - num_in_A - num_in_B
     result = num_in_C
     return result

print(solution())