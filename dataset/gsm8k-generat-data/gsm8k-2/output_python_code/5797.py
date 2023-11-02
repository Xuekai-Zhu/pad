def solution():
    """Lex is picking apples in his apple orchard when he notices some of the apples have bruises and some have worms. He wants to save the bruised apples to make applesauce, throw the wormy apples away, and keep the unbruised apples to eat raw. By his count, a fifth of the apples have worms and nine more than one fifth are bruised. He picked 85 apples. How many apples will he have left to eat raw?"""
    total_apples = 85
    wormy_apples = total_apples / 5
    bruised_apples = (1/5 * total_apples) + 9
    raw_apples = total_apples - wormy_apples - bruised_apples
    result = raw_apples
    return result

print(solution())