def solution():
    # Define the historical context
    event = "Prince's Crusade"
    goal = "take back Jerusalem from Islamic hands"
    # Check if being a leader in this event makes Godfrey of Bouillon an Islamaphobe
    if event == "Prince's Crusade" and goal != "establish peace and cooperation":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())