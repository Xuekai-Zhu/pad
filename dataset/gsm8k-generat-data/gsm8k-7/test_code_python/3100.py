def solution():
    bonnie_eaten = 60
    
    # Third dog likes bonnies
    blueberries_eaten = (4/3) * bonnie_eaten
    
    # Second dog likes blueberries
    apples_eaten = 3 * blueberries_eaten
    
    # First dog likes apples
    total_fruits = bonnie_eaten + blueberries_eaten + apples_eaten
    result = total_fruits
    return result

print(solution())