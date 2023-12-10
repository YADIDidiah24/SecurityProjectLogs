#!/bin/bash

log_file_path="/var/log/auth.log"  # Replace with the actual path to your log file
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
  # Logging the DOS attempt
  logger -t DosAttempt -p auth.notice "DoS attack detected on port 9080"

  block_traffic
  logger -t BlockTraffic -p auth.notice "Firewall has blocked all traffic"
  sleep 2  # Adjust the sleep interval as needed
else
  echo "Dos Attack Not Detected"
  # Logging that DOS was not detected
  logger -t DosTest -p auth.notice "No DoS attack was detected by the test"
fi

echo ""
echo "Dos Attack Check Complete"
exit 0
