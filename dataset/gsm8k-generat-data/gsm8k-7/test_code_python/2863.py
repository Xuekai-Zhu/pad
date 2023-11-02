def solution():
    num_homes = 20
    panels_per_home = 10
    panels_ordered = (num_homes * panels_per_home) - 50   # 50 panels less than required
    num_panels_installed = panels_ordered if panels_ordered <= (num_homes * panels_per_home) else (num_homes * panels_per_home)
    num_homes_installed = num_panels_installed // panels_per_home
    result = num_homes_installed
    return result

print(solution())