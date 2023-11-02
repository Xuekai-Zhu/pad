def solution():
    america_peak_lift = 300  # America can lift 300 pounds at her peak
    maya_start_lift = america_peak_lift / 4  # Maya can only lift a fourth of what America can

    # Maya adds 10 pounds to her previous lift until she reaches her absolute peak, which is half of America's lift
    maya_peak_lift = america_peak_lift / 2
    while maya_start_lift < maya_peak_lift:
        maya_start_lift += 10

    # Calculate how many more pounds Maya can lift now than when she started
    lift_increase = maya_start_lift - (america_peak_lift / 4)
    result = lift_increase
    return result

print(solution())