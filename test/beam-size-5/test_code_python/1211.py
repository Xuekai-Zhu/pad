def solution():
    
    jar_base = 6 * 6
    jar_height = 15
    jar_width = 6
    jar_height = 15
    jar_cubic_inches = jar_base * jar_height
    jar_cubic_inches_packing = jar_cubic_inches * 0.8
    jar_red_jelly_beans = jar_cubic_inches * 0.3
    jar_distance = jar_cubic_inches - jar_cubic_inches - jar_red_jelly_beans
    guess_red_jelly_beans = jar_distance / red_jelly_beans
    result = guess_red_jelly_beans
    return result

print(solution())