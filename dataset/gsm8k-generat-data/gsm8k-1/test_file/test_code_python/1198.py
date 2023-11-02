def solution():
    """Amy had two eyeshadow palettes with four colors each and three makeup sets that came with six eyeshadow colors each. Her sister steals one of the palettes. 
    Amy uses up half of the colors from one makeup set. How many eyeshadow colors does she have left?"""

    palettes = 2
    palette_colors = 4
    stolen_palettes = 1
    remaining_palettes = palettes - stolen_palettes
    makeup_sets = 3
    makeup_colors = 6
    used_makeup_sets = 0.5
    remaining_makeup_sets = makeup_sets - used_makeup_sets
    total_colors = (remaining_palettes * palette_colors) + (remaining_makeup_sets * makeup_colors)
    result = total_colors
    return result

print(solution())