def solution():
    """A clerk can process 25 forms per hour. If 2400 forms must be processed in an 8-hour day, how many clerks must you hire for that day?"""
    # Define the number of forms to be processed and the processing rate per clerk
    total_forms = 2400
    processing_rate = 25

    # Calculate the total processing time required in hours
    total_processing_time = total_forms / processing_rate

    # Calculate the number of clerks required
    clerks_required = total_processing_time / 8

    # Round up to the nearest whole number
    clerks_required = math.ceil(clerks_required)

    # return the result
    result = clerks_required
    return result

print(solution())