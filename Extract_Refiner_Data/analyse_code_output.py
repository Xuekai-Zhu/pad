import json
import csv
import re
from collections import defaultdict

# Define a regex pattern to match typical Python error types
error_pattern = re.compile(r'\b(\w+Error)\b')

def extract_error_type_with_regex(output):
    matches = error_pattern.findall(output)
    if matches:
        return matches[-1]
    else:
        return 'Unknown Error'

def analyze_json_file(file_path, csv_file_path):
    outcome_counts = defaultdict(int)

    # Read the file and process each line
    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_entry = json.loads(line.strip())
                if 'Error' in json_entry['output']:
                    error_type = extract_error_type_with_regex(json_entry['output'])
                    outcome_counts[error_type] += 1
                elif json_entry['output'] != json_entry['answer']:
                    outcome_counts['Non-matching Answers'] += 1
            except json.JSONDecodeError:
                outcome_counts['JSON Decode Error'] += 1
            except KeyError:
                outcome_counts['Missing Key Error'] += 1

    # Sort the counts for output
    sorted_outcome_counts = sorted(outcome_counts.items(), key=lambda item: item[1], reverse=True)

    # Write the counts to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Outcome', 'Count'])
        for outcome, count in sorted_outcome_counts:
            writer.writerow([outcome, count])

    return csv_file_path

# You can call the function with the paths to your files
# example_file_path = 'path_to_your_json_file.jsonl'
# example_csv_file_path = 'path_to_your_output.csv'
# analyze_json_file(example_file_path, example_csv_file_path)



# version 2 of code error analyse
import json
import pandas as pd

def analyze_errors(file_path):
    # Define a function to extract the error type from the output
    def extract_error_type(output):
        known_errors = [
            'AssertionError', 'AttributeError', 'EOFError', 'FloatingPointError',
            'GeneratorExit', 'ImportError', 'IndexError', 'KeyError', 'KeyboardInterrupt',
            'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError',
            'ReferenceError', 'RuntimeError', 'StopIteration', 'SyntaxError', 'IndentationError',
            'TabError', 'SystemError', 'SystemExit', 'TypeError', 'UnboundLocalError',
            'UnicodeError', 'UnicodeEncodeError', 'UnicodeDecodeError', 'UnicodeTranslateError',
            'ValueError', 'ZeroDivisionError'
        ]
        for error in known_errors:
            if error in output:
                return error
        return 'Unspecified Error'

    # Initialize a dictionary to keep track of error counts
    error_categories = {}

    # Process each line in the file
    with open(file_path, 'r') as file:
        for line in file:
            try:
                # Parse the JSON data from the line
                data = json.loads(line)
                output = data.get('output', '')

                # Check if the output contains an error type
                if "Error" in output:
                    error_type = extract_error_type(output)
                    error_categories[error_type] = error_categories.get(error_type, 0) + 1
                else:
                    # Increment count for non-matching answers
                    error_categories['Non-matching Answers'] = error_categories.get('Non-matching Answers', 0) + 1

            except json.JSONDecodeError:
                # Increment count for JSON decoding errors
                error_categories['JSONDecodeError'] = error_categories.get('JSONDecodeError', 0) + 1

    # Convert the error categories to a DataFrame
    df_error_counts = pd.DataFrame(list(error_categories.items()), columns=['Outcome', 'Count'])

    # Define the path for the CSV output
    csv_output_path = file_path.rsplit('.', 1)[0] + '_error_analysis.csv'

    # Save the DataFrame to a CSV file
    df_error_counts.to_csv(csv_output_path, index=False)

    return csv_output_path

# You can then call this function with the path to your JSON lines file like so:
# csv_file_path = analyze_errors('/path/to/your/results.wrong_sample')


if __name__ == '__main__':
    # v1
    example_file_path = 'Extract_Refiner_Data/gsm8k/code-t5-large-enhanced-7time-learning-6e-5/results.wrong_sample'
    example_csv_file_path = 'Extract_Refiner_Data/gsm8k/code-t5-large-enhanced-7time-learning-6e-5/wrong_sample.csv'
    analyze_json_file(example_file_path, example_csv_file_path)
    
    # v2
    # analyze_errors(example_file_path)