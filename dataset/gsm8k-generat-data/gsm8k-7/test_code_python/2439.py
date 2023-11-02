def solution():
    # Let's define the variables
    muscovy = 0
    cayuga = 0
    khaki_campbell = 0
    total_ducks = 90

    # Express the relationships between the variables in the problem
    muscovy = cayuga + 4
    cayuga = 2 * khaki_campbell + 3
    total_ducks = muscovy + cayuga + khaki_campbell

    # Solve the equations to find the value of muscovy
    khaki_campbell = (total_ducks - 7) / 5
    cayuga = 2 * khaki_campbell + 3
    muscovy = cayuga + 4

    result = muscovy
    return result

print(solution())