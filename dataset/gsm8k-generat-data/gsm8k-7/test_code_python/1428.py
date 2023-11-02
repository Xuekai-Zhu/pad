def solution():
    basswood_figures_per_block = 3
    butternut_figures_per_block = 4
    aspen_figures_per_block = 6  # twice the amount of basswood

    num_basswood_blocks = 15
    num_butternut_blocks = 20
    num_aspen_blocks = 20

    # Calculate the total number of figurines that can be made from all blocks of basswood
    total_basswood_figures = basswood_figures_per_block * num_basswood_blocks

    # Calculate the total number of figurines that can be made from all blocks of butternut
    total_butternut_figures = butternut_figures_per_block * num_butternut_blocks

    # Calculate the total number of figurines that can be made from all blocks of Aspen
    total_aspen_figures = aspen_figures_per_block * num_aspen_blocks

    # Calculate the total number of figurines that can be made from all blocks of wood
    total_figures = total_basswood_figures + total_butternut_figures + total_aspen_figures
    result = total_figures
    return result

print(solution())