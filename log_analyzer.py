import os
import re

# Directory containing the log files
log_directory = "logs"

# Pattern to find the specific logs with "1 - Peticions TCP" in CAMPO3
pattern = re.compile(r'<CAMPO1>INP</CAMPO1>.*<CAMPO3>1 - Peticions TCP</CAMPO3>')

# Counter for occurrences
occurrence_count = 0

# Iterate over each file in the directory
for file in os.listdir(log_directory):
    # Check if the file ends with a Julian date (a numeric extension)
    if file.split('.')[-1].isdigit():
        file_path = os.path.join(log_directory, file)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find all matches of the specific pattern in the file
            matches = pattern.findall(content)
            
            # Count the number of matches
            occurrence_count += len(matches)

# Display the result
print(f"Total number of '1 - Peticions TCP' entries found: {occurrence_count}")
