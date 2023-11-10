#!/bin/bash

# Simulate realistic failed login attempts

# Define an array of realistic usernames
usernames=("john.doe" "jane.smith" "admin" "user123" "alice")

# Define an IP address range or use real IP addresses
ip_range="192.168.1."

# Define an array of reasons for failed login attempts
fail_reasons=("Incorrect password" "Account locked" "Expired password")

for ((i=0; i<3; i++)); do
    username="${usernames[$((RANDOM % ${#usernames[@]}))]}"
    ip_address="$ip_range$((RANDOM % 256))"
    reason="${fail_reasons[$((RANDOM % ${#fail_reasons[@]}))]}"
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Generate a log entry for a failed login attempt using logger
    logger -t FailedLogin -p auth.warning "Failed login attempt for $username from IP $ip_address: $reason"
    
    # Sleep for a random duration between 1 and 5 seconds to simulate activity
    random_delay=$((1 + RANDOM % 5))
    sleep $random_delay
done

