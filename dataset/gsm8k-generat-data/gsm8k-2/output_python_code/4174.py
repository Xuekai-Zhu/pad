def solution():
    """The vending machine fails to drop a snack when it’s purchased one in six times. One in ten times, it will accidentally drop two snacks. The rest of the time, it drops the purchased snack. If thirty people have used the vending machine once each to purchase a snack, how many snacks has the vending machine dropped?"""
    num_people = 30
    fail_probability = 1/6
    double_drop_probability = 1/10
    normal_drop_probability = 1 - fail_probability - double_drop_probability
    total_snacks_dropped = fail_probability*num_people + 2*double_drop_probability*num_people
    
    result = total_snacks_dropped
    return result

print(solution())