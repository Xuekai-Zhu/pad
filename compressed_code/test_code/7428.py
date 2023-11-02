def solution():
    
    total_ducks = 40
    muscovy_percent = 50
    muscovy_ducks = total_ducks * (muscovy_percent / 100)
    female_percent = 30
    female_muscovy = muscovy_ducks * (female_percent / 100)
    result = female_muscovy
    return result

print(solution())