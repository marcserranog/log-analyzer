import os
import re
from datetime import datetime

# Directory containing the log files
log_directory = "logs"

# Pattern to find logs with "Iniciem el Servei de connexió TCP" in CAMPO9 and capture CAMPO5 and CAMPO9
pattern = re.compile(r'<Log>.*?<CAMPO5>(.*?)</CAMPO5>.*?<CAMPO9>Iniciem el Servei de connexió TCP</CAMPO9>.*?</Log>', re.DOTALL)

def process_file(file_path):
    logs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        buffer = ''
        for line in f:
            buffer += line
            while '<Log>' in buffer and '</Log>' in buffer:
                # Find the position of the first complete <Log> entry
                start = buffer.find('<Log>')
                end = buffer.find('</Log>', start) + len('</Log>')
                log_entry = buffer[start:end]
                
                # Search for matches within the extracted log entry
                match = pattern.search(log_entry)
                if match:
                    # Extract date and time from CAMPO5
                    date_str = match.group(1)
                    try:
                        # Parse the date string
                        date_obj = datetime.fromisoformat(date_str)
                        # Append to list as tuple (date_obj, message)
                        logs.append((date_obj, "El día {} se inició el servicio.".format(date_obj.strftime('%A %d %B %Y %H:%M:%S'))))
                    except ValueError:
                        # Handle case where date parsing fails
                        print(f"Fecha inválida encontrada en el log: {date_str}")
                
                # Update buffer to keep the remaining content after the last </Log> tag
                buffer = buffer[end:]
    
    return logs

# List to store all logs
all_logs = []

# Iterate over each file in the directory
for file in os.listdir(log_directory):
    if file.split('.')[-1].isdigit():
        file_path = os.path.join(log_directory, file)
        all_logs.extend(process_file(file_path))

# Sort logs by date, from most recent to oldest
all_logs.sort(reverse=True, key=lambda x: x[0])

# Display the result
print(f"Total number of 'Iniciem el Servei de connexió TCP' logs found: {len(all_logs)}")
for date, message in all_logs:
    print(message)
