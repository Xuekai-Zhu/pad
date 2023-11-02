def solution():
    
    bonnies_eaten = 60
    blueberries_eaten = (3/4) * bonnies_eaten
    apples_eaten = 3 * blueberries_eaten
    total_fruits_eaten = bonnies_eaten + blueberries_eaten + apples_eaten
    result = total_fruits_eaten
    return result

print(solution())