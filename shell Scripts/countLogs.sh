#!/bin/bash

log_file="/var/log/auth.log"

limit=$(date -d '2 hours ago' '+%s')

function print_login_details {
    type=$1
    count=$(strings "$log_file" | grep -w "$type" | awk -v limit="$limit" '{timestamp=strftime("%s", substr($0, 1, 25)); if (timestamp >= limit) count++} END {if (count == "") count = 0; print count}')

    echo "Total number of $type logins in the last 2 hours: $count"
    echo ""
    
    if [ "$count" -gt 0 ]; then
        echo "Details for $type logins are given below:"
        echo ""
        strings "$log_file" | grep -w "$type" | awk -v limit="$limit" '{timestamp=strftime("%s", substr($0, 1, 25)); if (timestamp >= limit) {for (i=10; i<=13; i++) printf $i" "; print ""}}' | sort -u
    else
        echo "No $type logins found in the last 2 hours."
    fi
    
    echo ""
}

# Print details for different types of logins
print_login_details "IncomingRequest"
print_login_details "SuccessfulLogin"
print_login_details "FailedLogin"
print_login_details "AuthorisedAccess"
print_login_details "UnauthorizedAccess"
