def solution():
    """Avery puts 4 shirts in the donation box. He adds twice as many pants as shirts in the box. He throws in half as many shorts as pants in the box. In total, how many pieces of clothes is Avery donating?"""
    shirts = 4
    pants = shirts * 2
    shorts = pants / 2
    total_clothes = shirts + pants + shorts
    result = total_clothes
    return result

print(solution())