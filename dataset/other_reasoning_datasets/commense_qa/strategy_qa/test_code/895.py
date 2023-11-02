def solution():
    secretary_of_state_role = "carries out the President's foreign policy"
    white_house_phone_lines = "managed by multiple people"
    if secretary_of_state_role != white_house_phone_lines:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())