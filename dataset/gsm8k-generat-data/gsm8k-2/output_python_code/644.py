def solution():
    """In the city, there is a block of flats. This block has 12 floors. Half of the floors have 6 apartments and the other half have 5 apartments. One apartment can accommodate a maximum of 4 residents. What is the maximum number of residents that can live in this block of flats?"""
    total_floors = 12
    half_floors = total_floors // 2
    six_apts_floors = half_floors
    five_apts_floors = total_floors - half_floors
    max_residents_per_apt = 4
    six_apt_residents = 6 * half_floors * 6 * max_residents_per_apt
    five_apt_residents = 5 * half_floors * 5 * max_residents_per_apt
    total_residents = six_apt_residents + five_apt_residents
    result = total_residents
    return result

print(solution())