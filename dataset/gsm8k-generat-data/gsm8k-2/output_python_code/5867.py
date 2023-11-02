def solution():
    """Jessie's community built a new hedge. Each section of the hedge used 30 pieces of concrete blocks that cost $2 per piece. The hedge has eight sections. How much did they spend on the concrete blocks?"""
    num_blocks_per_section = 30
    block_cost = 2
    num_sections = 8
    total_cost = num_blocks_per_section * block_cost * num_sections
    result = total_cost
    return result

print(solution())