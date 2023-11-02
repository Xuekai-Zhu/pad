def solution():
    homes = 20
    Solar_panels_needed = homes * 10
    Solar_panels_received = Solar_panels_needed - 50
    Solar_panels_installed = Solar_panels_received // 10
    result = Solar_panels_installed
    return result

print(solution())