def solution():
    """Jerry is cutting up wood for his wood-burning stove. Each pine tree makes 80 logs, each maple tree makes 60 logs, and each walnut tree makes 100 logs. If Jerry cuts up 8 pine trees, 3 maple trees, and 4 walnut trees, how many logs does he get?"""
    pine_logs = 80 * 8
    maple_logs = 60 * 3
    walnut_logs = 100 * 4
    total_logs = pine_logs + maple_logs + walnut_logs
    result = total_logs
    return result

print(solution())