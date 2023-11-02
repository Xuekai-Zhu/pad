def solution():
    # Define the relationships between autopilot, vehicles, engines, and fossil fuels
    uses_autopilot = True
    powered_by_engine = True
    relies_on_fossil_fuels = True
    # Check if autopilot relies on fossil fuels
    if uses_autopilot and powered_by_engine and relies_on_fossil_fuels:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())