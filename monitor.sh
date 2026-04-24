#!/bin/bash

# 1. CPU Usage (Windows/Git Bash friendly way)
# Agar 'top' nahi hai, toh hum WMIC use karenge (Windows specific)
if command -v top &> /dev/null
then
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
else
    # Windows fallback
    cpu_usage="15.5" # Filhal static rakhte hain testing ke liye
fi

# 2. RAM Usage
if command -v free &> /dev/null
then
    ram_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
else
    # Windows fallback logic
    ram_usage="45.2"
fi

# 3. Disk Usage (Ye tumhare mein chal raha hai)
disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

# 4. System Uptime (Human Readable)
uptime_val=$(uptime -p | sed 's/up //')

echo "UPTIME:$uptime_val"

echo "CPU:$cpu_usage"
echo "RAM:$ram_usage"
echo "DISK:$disk_usage"