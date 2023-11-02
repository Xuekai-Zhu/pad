def solution():
    
    tallest_trees = 30
    shortest_trees = tallest_trees / 2
    average_trees = tallest_trees + shortest_trees + 1
    joanne_apples = tallest_trees * 2
    sister_apples = shortest_trees * 3
    total_apples = 500
    joanne_apples_gathered = joanne_apples + sister_apples
    sister_apples_gathered = total_apples - joanne_apples - sister_apples
    result = sister_apples_gathered
    return result

print(solution())