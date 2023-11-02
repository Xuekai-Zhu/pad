def solution():
    # Define the facts about Drew Carey's involvement in wrestling
    royal_rumble_participant = True
    WWE_Hall_of_Famer = True
    # Check if Drew Carey is important to the history of wrestling
    if royal_rumble_participant or WWE_Hall_of_Famer:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())