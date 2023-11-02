def solution():
    temp1 = -14
    temp2 = -8
    temp3 = 1
    avg_temp = (temp1 + temp2 + temp3) / 3
    result = avg_temp
    return result

 Question: Every day, 4 people use the stairs in the city hall. 2 people use the stairs going up, and 2 people use the stairs going down. There are a total of 10 steps in the stairs. How many steps are climbed every day, in total?
 Solution:
def solution():
    people_upstairs = 2
    people_downstairs = 2
    people_total = people_upstairs + people_downstairs
    steps_upstairs = people_upstairs * 10
    steps_downstairs = people_downstairs * 10
    total_steps = steps_upstairs + steps_downstairs
    result = total_steps
    return result

print(solution())