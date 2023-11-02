def solution():
    # Calculate the total number of panels needed
    total_panels = 20 * 10  

    # Calculate the number of panels supplied by the supplier
    supplied_panels = total_panels - 50  

    # Calculate the number of homes that had their panels installed
    homes_installed = supplied_panels // 10  
    result = homes_installed
    return result

print(solution())