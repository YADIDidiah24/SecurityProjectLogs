#!/bin/bash
# Define authorized user accounts
authorized_users=("user1" "user2" "user3")
# Simulate access attempts
for ((i=0; i<7; i++)); do
    username="user$((RANDOM % 10))"
    ip_address="192.168.1.$((RANDOM % 256))"
    # Check if the generated user is authorized
    if [[ " ${authorized_users[*]} " =~ " $username " ]]; then
        # Log the authorized access using the logger command
        logger -t AuthorizedAccess -p auth.notice "Authorized access by $username from IP $ip_address"
    else
        timestamp=$(date +"%Y-%m-%d %H:%M:%S")
        # Generate a log entry for an unauthorized access attempt using logger
        logger -t UnauthorizedAccess -p auth.notice "Unauthorized access attempt by $username from IP $ip_address"
    fi
    # Generate a random delay between 1 and 5 seconds
    random_delay=$((1 + RANDOM % 5))
    sleep $random_delay
done
