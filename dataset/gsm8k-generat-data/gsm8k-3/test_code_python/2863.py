def solution():
    """Faith's neighborhood, with a total of 20 homes, decided to install solar panels. Each home needed 10 panels capable of providing their power needs. The supplier of the panels brought 50 panels less than the required amount. The neighbors agreed to only install the panels up to where they'd be finished. How many homes had their panels installed?"""
    # Define the number of homes and panels needed per home
    NUM_HOMES = 20
    PANELS_PER_HOME = 10

    # Calculate the total number of panels needed
    total_panels_needed = NUM_HOMES * PANELS_PER_HOME

    # Calculate the number of panels supplied
    panels_supplied = total_panels_needed - 50

    # Calculate the number of homes that had their panels installed
    homes_with_panels = panels_supplied // PANELS_PER_HOME

    # Display the number of homes with panels installed
    result = homes_with_panels
    return result

print(solution())