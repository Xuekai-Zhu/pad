def solution():
    first_tree_red_percent = 40
    first_tree_green_percent = 60
    first_tree_total_percent = 100
    second_tree_red_percent = 50
    second_tree_green_percent = 50
    second_tree_total_percent = 100
    first_tree_red_apples = first_tree_red_percent / first_tree_total_percent * 20
    second_tree_red_apples = second_tree_red_percent / second_tree_total_percent * 20
    total_red_apples = first_tree_red_apples + second_tree_red_apples
    result = total_red_apples
    return result

Question: The tablecloth in the dining hall is rectangular.  It is 8 feet wide and 20 feet long.  How much fabric does it take to make this tablecloth?
 Solution: 
def solution():
    width = 8
    length = 20
    area = width * length
    result = area
    return result

print(solution())