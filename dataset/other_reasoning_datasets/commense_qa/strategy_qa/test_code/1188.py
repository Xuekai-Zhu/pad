def solution():
    ib_wolf_habitat = ["northern Portugal", "northwestern Spain"]
    southern_us_states = ["Alabama", "Arkansas", "Florida", "Georgia", "Louisiana", "Mississippi", "Oklahoma", "Texas"]
    # Check if the Iberian wolf habitat and Southern US states have any overlap
    overlap = [state for state in southern_us_states if state in ib_wolf_habitat]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())