def solution():
    """John cuts down an 80-foot tree. He can make logs out of 80% of it. He cuts it into 4-foot logs. From each of those logs, he cuts 5 planks. He then sells each plank for $1.2. How much does he make?"""
    tree_height = 80
    log_percentage = 0.8
    log_height = 4
    planks_per_log = 5
    plank_price = 1.2
    
    usable_tree_height = tree_height * log_percentage
    total_logs = usable_tree_height / log_height
    total_planks = total_logs * planks_per_log
    money_made = total_planks * plank_price
    
    result = money_made
    return result

print(solution())