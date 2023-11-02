def solution():
    """Andy started out the year weighing 156 pounds. He then grew 3 inches and gained 36 pounds. Andy wasn't happy with his weight and decided to exercise. Over the next 3 months, he lost an eighth of his weight every month. How much less does Andy weigh now than at the beginning of the year?"""
    # Define Andy's initial weight and growth
    initial_weight = 156
    growth_pounds = 36

    # Define the weight and growth conversion factors
    weight_conversion = 1/2.2
    growth_conversion = 2.54

    # Convert weight and growth to metric units
    initial_weight_metric = initial_weight * weight_conversion
    growth_metric = growth_pounds * weight_conversion
    growth_height_metric = 3 * growth_conversion

    # Calculate Andy's BMI before exercise
    height_metric = (68 + growth_height_metric) / 100
    bmi_before = initial_weight_metric / height_metric**2

    # Define the weight loss over 3 months
    weight_loss = (1/8) * initial_weight_metric

    # Calculate weight and BMI after 3 months of exercise
    final_weight_metric = initial_weight_metric - (3 * weight_loss)
    height_metric = (71 + growth_height_metric) / 100
    bmi_after = final_weight_metric / height_metric**2

    # Calculate the difference in weight and BMI
    weight_difference = (initial_weight_metric - final_weight_metric) / weight_conversion
    bmi_difference = bmi_before - bmi_after

    # Return the weight difference
    result = round(weight_difference)
    return result

print(solution())