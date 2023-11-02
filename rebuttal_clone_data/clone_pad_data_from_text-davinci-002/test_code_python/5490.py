def solution():
    rabbits = 16
    Monday_toys = 6
    Wednesday_toys = Monday_toys * 2
    Friday_toys = Monday_toys * 4
    Saturday_toys = Wednesday_toys / 2
    total_toys = Monday_toys + Wednesday_toys + Friday_toys + Saturday_toys
    toys_per_rabbit = total_toys / rabbits
    result = toys_per_rabbit
    return result

print(solution())