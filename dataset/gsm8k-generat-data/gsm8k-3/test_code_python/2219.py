def solution():
    """Job is a farmer who rears cattle and grows crops. In total he has 150 hectares of land. 25 hectares are occupied by his house and farm machinery, and 15 hectares have been reserved for future expansion. 40 hectares are dedicated to rearing cattle. Assuming the rest of his land is used for crops, how many hectares of land does Job use for crop production?"""
    # Define the total size of Job's land
    total_land = 150

    # Define the size of land occupied by Job's house and farm machinery
    house_and_machinery = 25

    # Define the size of land reserved for future expansion
    future_expansion = 15

    # Define the size of land dedicated to rearing cattle
    cattle_land = 40

    # Calculate the total size of land used for non-crop purposes
    non_crop_land = house_and_machinery + future_expansion + cattle_land

    # Calculate the size of land used for crops
    crop_land = total_land - non_crop_land

    # Display the size of land used for crops
    result = crop_land
    return result

print(solution())