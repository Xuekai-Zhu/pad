def solution():
    """Teagan saved 200 pennies in her piggy bank. Rex has a mason jar filled with 100 nickels. Toni has 330 dimes stashed inside a giant mug. How much money did the three kids save altogether?"""
    teagan_pennies = 200
    rex_nickels = 100 * 5
    toni_dimes = 330 * 10
    total_cents = teagan_pennies + rex_nickels + toni_dimes
    total_dollars = total_cents / 100
    result = total_dollars
    return result

print(solution())