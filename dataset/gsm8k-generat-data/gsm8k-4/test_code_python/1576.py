def solution():
    """When Pogo, the four-legged martian, walks across the soft Martian soil, it leaves 4 footprints every meter.  But Grimzi, the three-legged Plutonian, leaves only 3 footprints in the soft sands of Pluto for every 6 meters it walks.  If Pogo travels 6000 meters across the soil of Mars, and Grimzi travels for 6000 meters across the fine sands of Pluto, what is the combined total number of footprints the two creatures will leave on the surfaces of their respective planets?"""
    # Calculate the number of footprints per meter for Pogo and Grimzi
    pogo_footprints_per_meter = 4
    grimzi_footprints_per_meter = 3/6

    # Calculate the total number of footprints left by Pogo and Grimzi in their respective planets
    pogo_footprints_total = pogo_footprints_per_meter * 6000
    grimzi_footprints_total = grimzi_footprints_per_meter * 6000

    # Calculate the combined total number of footprints left by Pogo and Grimzi
    combined_footprints = pogo_footprints_total + grimzi_footprints_total

    # return the result
    result = combined_footprints
    return result

print(solution())