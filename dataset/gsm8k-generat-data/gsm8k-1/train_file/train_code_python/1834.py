def solution():
    """Teagan saved 200 pennies in her piggy bank. Rex has a mason jar filled with 100 nickels. Toni has 330 dimes stashed inside a giant mug. How much money did the three kids save altogether?"""
    pennies = 200
    nickels = 100 * 5
    dimes = 330 * 10
    total = (pennies + nickels + dimes) / 100
    result = total
    return result

print(solution())