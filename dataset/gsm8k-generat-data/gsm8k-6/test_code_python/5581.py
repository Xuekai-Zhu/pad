def solution():
    # Calculate the number of students who wear glasses and contact lenses
    glasses_wearers = 0.25 * 40
    contacts_wearers = 0.4 * 40

    # Calculate the number of students who do not wear any vision assistance
    no_vision_assistance = 40 - glasses_wearers - contacts_wearers
    result = no_vision_assistance
    return result

print(solution())