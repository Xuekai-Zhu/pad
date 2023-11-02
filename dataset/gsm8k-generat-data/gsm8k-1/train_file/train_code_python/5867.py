def solution():
    """Jessie's community built a new hedge. Each section of the hedge used 30 pieces of concrete blocks that cost $2 per piece. The hedge has eight sections. How much did they spend on the concrete blocks?"""
    blocks_per_section = 30
    cost_per_block = 2
    sections = 8
    total_blocks = blocks_per_section * sections
    total_cost = total_blocks * cost_per_block
    result = total_cost
    return result

print(solution())