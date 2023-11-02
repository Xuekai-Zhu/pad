def solution():
    """Ophelia and Jenna are living in the same apartment building. They each have 2 fewer sofas than chairs. Jenna has 3 times as many chairs as Ophelia. If Ophelia has 20 sofas, calculate the total number of sofas and chairs that they have."""
    ophelia_sofas = 20
    ophelia_chairs = ophelia_sofas + 2
    jenna_chairs = 3 * ophelia_chairs
    jenna_sofas = jenna_chairs - 2
    total_sofas = ophelia_sofas + jenna_sofas
    total_chairs = ophelia_chairs + jenna_chairs
    result = total_sofas + total_chairs
    return result

print(solution())