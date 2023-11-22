from transformers import AutoTokenizer
import re
import numpy as np
import subprocess

# Define the Python code as a string
python_code = """
def solution():
    movie_c_length = 1.25 * 60
    movie_b_length = movie_c_length + 5
    movie_a_length = movie_b_length / 4
    result = movie_a_length
    return result

print(solution())
"""

# Run the Python code as a separate process
# The code is passed to the Python interpreter via stdin
process = subprocess.run(
    ['python', '-c', python_code],
    text=True,  # Use textual input and output
    capture_output=True,  # Capture stdout and stderr
    timeout=30  # Set a timeout for the operation
)
print(pro)
