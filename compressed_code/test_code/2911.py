def solution():
    
    dolls = 12000
    shoes = dolls * 2
    bags = dolls * 3
    cosmetics = dolls * 1
    hats = dolls * 5

    total_time = (dolls * 45) + (shoes * 10) + (bags * 10) + (cosmetics * 10) + (hats * 10)

    result = total_time
    return result

print(solution())