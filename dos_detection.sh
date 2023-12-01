#!/bin/bash

log_file_path="/var/log/auth.log"  # Replace with the actual path to your log file
dos_log="/var/log/dos.log"  # Specify the path for the DoS attack log
threshold_requests=10000
threshold_duration=60  # in seconds

block_traffic() {
  # Clear existing rules for port 9080
  sudo iptables -D INPUT -p tcp --dport 9080 -j ACCEPT
  sudo iptables -D INPUT -p tcp --dport 9080 -j REJECT --reject-with icmp-port-unreachable

  # Add the reject rule
  sudo iptables -A INPUT -p tcp --dport 9080 -j REJECT --reject-with icmp-port-unreachable
}

start_time=$(date -d "-${threshold_duration} seconds" +%s)
current_time=$(date +%s)

requests=$(awk -v start_time="$start_time" -v current_time="$current_time" \
  '$1 > start_time { requests++ } END { print requests }' "$log_file_path")

if [ "$requests" -gt "$threshold_requests" ]; then
  echo "DoS attack detected! Blocking incoming traffic..."
  block_traffic
  
  # Extract username and IP address from the log file (adjust accordingly based on your log format)
  username=$(awk '$NF == "Failed" { print $(NF-1) }' "$log_file_path")
  ip_address=$(awk '$NF == "Failed" { print $(NF-3) }' "$log_file_path")
  
  # Log the DoS attack
  logger -t "DoS attack" -p auth.notice "DoS attack attempt by $username from IP $ip_address"
  
  sleep 2  # Adjust the sleep interval as needed
fi

echo "Dos Attack Stopped"
exit 0
