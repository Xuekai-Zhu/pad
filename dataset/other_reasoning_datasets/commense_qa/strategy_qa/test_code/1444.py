def solution():
    is_newspeak_straightforward = False
    if "straightforward" in Newspeak:
        is_newspeak_straightforward = True
    else:
        is_newspeak_straightforward = False
    return is_newspeak_straightforward

print(solution())