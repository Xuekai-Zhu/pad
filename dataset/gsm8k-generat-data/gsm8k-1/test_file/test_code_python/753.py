def solution():
    """Krissa needs to order field trip shirts for her preschool students. 11 students need size extra-small. Twice as many students need size small as extra small.
    Four less than the number of size small students need size medium. Half as many students need size large as size medium.
    Six more students need size extra-large than large. Altogether, how many shirts did Krissa order?"""
    xs = 11
    s = 2*xs
    m = s-4
    l = m/2
    xl = l+6
    total_shirts = xs+s+m+l+xl
    result = total_shirts
    return result

print(solution())