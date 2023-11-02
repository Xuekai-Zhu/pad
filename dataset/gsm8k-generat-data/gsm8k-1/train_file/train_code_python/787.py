def solution():
    """Karen has 32 quarters in her piggy bank. Her older brother Christopher has 64 quarters in his piggy bank. How much more money does Christopher have?"""
    karen_quarters = 32
    christopher_quarters = 64
    quarter_value = 0.25
    karen_money = karen_quarters * quarter_value
    christopher_money = christopher_quarters * quarter_value
    difference = christopher_money - karen_money
    result = difference
    return result

print(solution())