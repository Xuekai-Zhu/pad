def solution():
    """Jennie is helping at her mom's office. She has a pile of 60 letters needing stamps, and a pile of letters already stamped. She puts stamps on one-third of the letters needing stamps. If there are now 30 letters in the pile of already-stamped letters, how many were in that pile when Jennie began?"""
    letters_needing_stamps = 60
    stamped_fraction = 1/3
    stamped_letters = 30
    unstamped_letters = letters_needing_stamps * (1 - stamped_fraction)
    total_letters = stamped_letters + unstamped_letters
    result = total_letters
    return result

print(solution())