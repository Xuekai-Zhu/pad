def solution():
    muffins = 95
    muffins_per_box = 5
    available_boxes = 10
    needed_boxes = (muffins // muffins_per_box) - available_boxes
    result = needed_boxes
    return result

 Question: There are 1,000 students in a school. Each student has 2 pencils. In total, how many pencils are in the school?
 Solution:
 def solution():
    students = 1000
    pencils_per_student = 2
    total_pencils = students * pencils_per_student
    result = total_pencils
    return result

print(solution())