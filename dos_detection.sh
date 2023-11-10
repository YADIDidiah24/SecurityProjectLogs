#!/bin/bash

log_file_path="/var/log/auth.log"  # Replace with the actual path to your log file
threshold_requests=10000
threshold_duration=60  # in seconds

start_time=$(date -d "-${threshold_duration} seconds" +%s)
current_time=$(date +%s)

block_traffic() {
  # Replace with the actual iptables command to block incoming traffic
  sudo iptables -A INPUT -p tcp --dport 9080 -j REJECT
}

requests=$(awk -v start_time="$start_time" -v current_time="$current_time" \
  '$1 > start_time { requests++ } END { print requests }' "$log_file_path")

if [ "$requests" -gt "$threshold_requests" ]; then
  echo "DoS attack detected! Blocking incoming traffic..."
  block_traffic
fi
echo "Dos Attack Stopped"
exit 0

