def solution():
    lasagna_mince = 2
    cottage_pie_mince = 3
    total_lasagna = 100
    total_mince = 500
    cottage_pie = (total_mince - (total_lasagna * lasagna_mince)) / cottage_pie_mince
    result = cottage_pie
    return result

print(solution())