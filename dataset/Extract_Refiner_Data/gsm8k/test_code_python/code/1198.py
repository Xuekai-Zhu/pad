def solution():
    
    # Define the number of eyeshadow colors in each palette and makeup set
    palettes_per_palette = 4
    makeup_sets_per_makeup = 6

    # Calculate the total number of eyeshadow colors
    total_colors = 2 * palettes_per_palette + 3 * makeup_sets_per_makeup

    # Subtract the colors stolen by Amy's sister
    total_colors -= palettes_per_palette

    # Calculate the number of colors used up by Amy from one makeup set
    colors_used_up = total_colors / 2

    # Subtract the colors used up by Amy from the total colors
    total_colors -= colors_used_up

    # Display the number of eyeshadow colors left
    result = total_colors
    return result

print(solution())