def solution():
    # Define the Android version running on the first Samsung Galaxy device
    android_version = "cupcake"
    # Check if the Android version sounds edible
    if "cupcake" in ["donut", "eclair", "froyo", "gingerbread", "honeycomb", "ice cream sandwich", "jelly bean", "kitkat", "lollipop", "marshmallow", "nougat", "oreo", "pie"]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())