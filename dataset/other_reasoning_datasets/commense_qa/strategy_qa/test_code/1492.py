def solution():
    # Define the possible locations for the MLB World Series
    mlb_locations = ["United States", "Canada"]
    # Check if Newcastle, New South Wales is within these locations
    if "New South Wales" in mlb_locations:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())