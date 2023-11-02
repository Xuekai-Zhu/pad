def solution():
    # Calculate the total number of panels needed
    total_panels_needed = 20 * 10

    # Calculate the number of panels the supplier brought
    panels_brought = total_panels_needed - 50

    # Calculate the number of homes that can have their panels installed
    homes_with_panels = panels_brought // 10

    result = homes_with_panels
    return result

print(solution())