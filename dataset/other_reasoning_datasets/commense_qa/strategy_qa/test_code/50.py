def solution():
    ubuntu_software = "free and open-source software"
    ubuntu_people_language = "Nguni Bantu"
    africa_computer_ownership = 0.1
    if ubuntu_people_language == ubuntu_software and africa_computer_ownership < 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())