def solution():
    old_english = "earliest form of English"
    modern_english = "replaced old English during seventeenth century"
    american_english = "created and spoken during first US colonies"
    confederate_states = "southern states"
    if old_english not in confederate_states:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())