def solution():
    # Define the components of soup, shoe soup, and factors related to Werner Herzog
    soup_components = ["liquid", "meat", "beans"]
    shoe_soup_components = ["liquid", "meat", "beans", "shoe"]
    werner_herzog_birthyear = 1942
    werner_herzog_age = 2019 - werner_herzog_birthyear
    werner_herzog_works_on_mandalorian = True
    
    # Check if shoe soup is innocuous
    if set(shoe_soup_components).issubset(soup_components) and werner_herzog_age >= 18 and werner_herzog_works_on_mandalorian:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())