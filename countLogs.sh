#!/bin/bash

log_file_path="/var/log/auth.log"  # Replace with the actual path to your log file

# Calculate the start time for the last hour
start_time=$(date -d "1 hour ago" "+%Y-%m-%dT%H:%M:%S")

# Count the occurrences of different log types from the last hour
num_incoming_requests=$(awk -v start_time="$start_time" '/IncomingRequest/ && $1 >= start_time { count++ } END { print count+0 }' "$log_file_path")
num_failed_login=$(awk -v start_time="$start_time" '/FailedLogin/ && $1 >= start_time { count++ } END { print count+0 }' "$log_file_path")
num_successful_login=$(awk -v start_time="$start_time" '/SuccessfulLogin/ && $1 >= start_time { count++ } END { print count+0 }' "$log_file_path")
num_unauthorized_access=$(awk -v start_time="$start_time" '/UnauthorizedAccess/ && $1 >= start_time { count++ } END { print count+0 }' "$log_file_path")
num_authorized_access=$(awk -v start_time="$start_time" '/AuthorizedAccess/ && $1 >= start_time { count++ } END { print count+0 }' "$log_file_path")
num_suspicious_download=$(awk -v start_time="$start_time" '/SuspiciousDownload/ && $1 >= start_time { count++ } END { print count+0 }' "$log_file_path")

# Print the counts
echo "Number of IncomingRequest: $num_incoming_requests"
echo "Number of FailedLogin: $num_failed_login"
echo "Number of SuccessfulLogin: $num_successful_login"
echo "Number of UnauthorizedAccess: $num_unauthorized_access"
echo "Number of AuthorizedAccess: $num_authorized_access"
echo "Number of SuspiciousDownload: $num_suspicious_download"
