def solution():
    """Faith's neighborhood, with a total of 20 homes, decided to install solar panels. Each home needed 10 panels capable of providing their power needs. The supplier of the panels brought 50 panels less than the required amount. The neighbors agreed to only install the panels up to where they'd be finished. How many homes had their panels installed?"""
    # Define the total number of homes and the number of panels required per home
    total_homes = 20
    panels_per_home = 10

    # Calculate the total number of panels required
    total_panels_required = total_homes * panels_per_home

    # Calculate the number of panels provided by the supplier
    panels_provided = total_panels_required - 50

    # Calculate the number of homes that can be fully installed
    homes_with_panels = panels_provided // panels_per_home

    # return the result
    result = homes_with_panels
    return result

print(solution())