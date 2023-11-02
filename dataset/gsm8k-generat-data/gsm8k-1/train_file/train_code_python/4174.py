def solution():
    """The vending machine fails to drop a snack when it’s purchased one in six times. One in ten times, it will accidentally drop two snacks. The rest of the time, it drops the purchased snack. If thirty people have used the vending machine once each to purchase a snack, how many snacks has the vending machine dropped?"""
    total_people = 30
    fail_rate = 1 / 6
    double_drop_rate = 1 / 10
    regular_drop_rate = 1 - fail_rate - double_drop_rate
    total_snacks_dropped = fail_rate * total_people + double_drop_rate * total_people * 2
    result = total_snacks_dropped
    return result

print(solution())