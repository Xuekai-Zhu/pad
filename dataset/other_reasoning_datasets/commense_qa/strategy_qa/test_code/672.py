def solution():
    is_naruto_a_ninja = True
    ninja_tactics_are_dishonorable = True
    # Check if Hattori Hanzō would admire Naruto
    if is_naruto_a_ninja and not ninja_tactics_are_dishonorable:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())