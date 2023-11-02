def solution():
    """David has a store where he sells cell phones. When he takes inventory at the end of the day, he notices that 
    he has 10 Samsung cell phones but he started the day with 14 Samsung cell phones. Then he notices that he has 5 
    iPhones and in the initial inventory, but started with 8. His staff then told him that in the afternoon they 
    realized that 2 Samsung cell phones were damaged and 1 iPhone had a manufacturing defect in the screen, so they 
    threw these out during the day. What was the total number of cell phones that were sold today?"""
    
    initial_samsung = 14
    final_samsung = 10
    damaged_samsung = 2
    
    initial_iphones = 8
    final_iphones = 5
    defective_iphones = 1
    
    sold_samsung = initial_samsung - final_samsung + damaged_samsung
    sold_iphones = initial_iphones - final_iphones + defective_iphones
    
    total_sold = sold_samsung + sold_iphones
    result = total_sold
    
    return result

print(solution())