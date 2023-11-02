def solution():
    """Faith's neighborhood, with a total of 20 homes, decided to install solar panels. Each home needed 10 panels capable of providing their power needs. The supplier of the panels brought 50 panels less than the required amount. The neighbors agreed to only install the panels up to where they'd be finished. How many homes had their panels installed?"""
    total_homes = 20
    panels_per_home = 10
    total_panels_needed = total_homes * panels_per_home
    panels_supplied = total_panels_needed - 50
    homes_with_panels = panels_supplied // panels_per_home
    result = homes_with_panels
    return result

print(solution())