def solution():
    
    total_homes = 20
    panels_per_home = 10
    total_panels_needed = total_homes * panels_per_home
    panels_supplied = total_panels_needed - 50
    homes_with_panels = panels_supplied // panels_per_home
    result = homes_with_panels
    return result

print(solution())