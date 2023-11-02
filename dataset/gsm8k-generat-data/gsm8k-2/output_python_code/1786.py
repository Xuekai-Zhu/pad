def solution():
    """Kira is making breakfast for herself. She fries 3 sausages then scrambles 6 eggs and cooks each item of food separately. If it takes 5 minutes to fry each sausage and 4 minutes to scramble each egg then how long, in minutes, did it take for Kira to make her breakfast?"""
    sausages = 3
    eggs = 6
    sausage_time = 5
    egg_time = 4
    total_time = (sausages * sausage_time) + (eggs * egg_time)
    result = total_time
    return result

print(solution())