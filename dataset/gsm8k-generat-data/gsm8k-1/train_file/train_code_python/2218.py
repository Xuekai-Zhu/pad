def solution():
    """Job is a farmer who rears cattle and grows crops. In total he has 150 hectares of land. 25 hectares are occupied by his house and farm machinery, and 15 hectares have been reserved for future expansion. 40 hectares are dedicated to rearing cattle. Assuming the rest of his land is used for crops, how many hectares of land does Job use for crop production?"""
    total_land = 150
    house_and_machinery = 25
    future_expansion = 15
    cattle_land = 40
    crop_land = total_land - house_and_machinery - future_expansion - cattle_land
    result = crop_land
    return result

print(solution())