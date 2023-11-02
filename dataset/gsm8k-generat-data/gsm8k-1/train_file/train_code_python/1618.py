def solution():
    """Ragnar is a woodchopper. He can get 3 blocks of wood for every tree he cuts. If Ragnar chops 2 trees every day, how many blocks of woods does he get after 5 days?"""
    trees_per_day = 2
    blocks_per_tree = 3
    days = 5
    total_blocks = trees_per_day * blocks_per_tree * days
    result = total_blocks
    return result

print(solution())