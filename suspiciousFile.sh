#!/bin/bash

# Simulate suspicious file downloads for legitimate security testing

# Define a function to generate random usernames
generate_username() {
    usernames=("user1" "user2" "user3" "user4" "user5")
    random_index=$((RANDOM % ${#usernames[@]}))
    echo "${usernames[$random_index]}"
}

# Define a function to generate random file paths
generate_file_path() {
    files=("/var/www/files/suspiciousfile1.zip" "/var/www/files/suspiciousfile2.zip" "/var/www/files/suspiciousfile3.zip")
    random_index=$((RANDOM % ${#files[@]}))
    echo "${files[$random_index]}"
}

# Define the number of iterations
iterations=10

# Run the simulation for the specified number of times
for ((i=1; i<=iterations; i++)); do
    username=$(generate_username)
    file_path=$(generate_file_path)
    
    # Generate a log entry for a suspicious file download using logger
    logger -t SuspiciousDownloads -p auth.notice "Suspicious file download by user $username: $file_path"
    
    # Sleep for a random duration between 1 and 5 seconds to simulate activity
    random_delay=$((1 + RANDOM % 5))
    sleep $random_delay
done
