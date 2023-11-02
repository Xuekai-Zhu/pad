def solution():
    
    total_ducks = 40
    muscovy_percentage = 0.5
    muscovy_ducks = muscovy_percentage * total_ducks
    female_percentage = 0.3
    female_muscovy_ducks = muscovy_ducks * female_percentage
    result = female_muscovy_ducks
    return result

print(solution())