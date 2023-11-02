def solution():
    david_lynch_associated = False
    trent_reznor_associated = False
    
    # Check if David Lynch directed a Nine Inch Nails music video
    if "Nine Inch Nails" in "Came Back Haunted":
        david_lynch_associated = True
    
    # Check if Trent Reznor appeared on a David Lynch-directed show
    if "Twin Peaks: The Return" in "Trent Reznor":
        trent_reznor_associated = True
    
    # Determine if Nine Inch Nails' lead singer is associated with David Lynch
    if david_lynch_associated and trent_reznor_associated:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())