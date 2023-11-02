def solution():
    """When Pogo, the four-legged martian, walks across the soft Martian soil, it leaves 4 footprints every meter.  But Grimzi, the three-legged Plutonian, leaves only 3 footprints in the soft sands of Pluto for every 6 meters it walks.  If Pogo travels 6000 meters across the soil of Mars, and Grimzi travels for 6000 meters across the fine sands of Pluto, what is the combined total number of footprints the two creatures will leave on the surfaces of their respective planets?"""
    # Calculate the number of footprints Pogo leaves on Mars
    pogo_footprints = 4 * 6000

    # Calculate the number of footprints Grimzi leaves on Pluto
    grimzi_footprints = (3/6) * 6000 * 3

    # Calculate the total number of footprints left on both planets
    total_footprints = pogo_footprints + grimzi_footprints

    # Display the total number of footprints
    result = total_footprints
    return result

print(solution())