def solution():
    """To make pizza, together with other ingredients, Kimber needs 10 cups of water, 16 cups of flour, and 1/2 times as many teaspoons of salt as the number of cups of flour. Calculate the combined total number of cups of water, flour, and teaspoons of salt that she needs to make the pizza."""
    cups_water = 10
    cups_flour = 16
    teaspoons_salt = 0.5 * cups_flour
    total = cups_water + cups_flour + teaspoons_salt
    result = total
    return result

print(solution())