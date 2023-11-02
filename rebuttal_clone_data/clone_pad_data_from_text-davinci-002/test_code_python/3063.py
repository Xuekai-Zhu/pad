def solution():
    experience_roger = 50
    experience_peter = 19
    experience_tom = experience_roger / 2
    experience_robert = experience_peter - 4
    experience_mike = experience_robert - 2
    total_experience = experience_roger + experience_peter + experience_tom + experience_robert + experience_mike
    result = experience_roger - total_experience
    return result
    
 Question: John has a total of 21 chocolates. He wants to divide them into 3 bags such that each bag has an odd number of chocolates and the difference between the number of chocolates in any two bags is as large as possible. How many chocolates should be in each bag?
 Solution:
def solution():
    total_chocolates = 21
    bag_1 = total_chocolates / 3 + 1
    bag_2 = bag_1 - 2
    bag_3 = bag_2 - 2
    result = [bag_1, bag_2, bag_3]
    return result

print(solution())