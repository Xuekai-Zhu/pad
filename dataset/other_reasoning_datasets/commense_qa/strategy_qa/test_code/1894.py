def solution():
    original_platform = "Nintendo Entertainment System"
    graphics_style = "2-D pixel-art"
    playable_female_protagonist = True
    groundbreaking_polygons = False
    
    if original_platform != "Sony Playstation" and not groundbreaking_polygons and playable_female_protagonist:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())