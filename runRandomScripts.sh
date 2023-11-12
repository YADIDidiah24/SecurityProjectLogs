#!/bin/bash

# Number of times to run each script
num_runs=20

# Array of script names
scripts=("failedLogin.sh" "suspiciousFile.sh" "unauthorised.sh")

# Function to run a script randomly
run_random_script() {
  # Randomly select a script from the array
  random_script=${scripts[$((RANDOM % ${#scripts[@]}))]}

  # Run the selected script
  ./"$random_script"
}

# Run scripts randomly
for ((i = 1; i <= num_runs; i++)); do
  echo "Run $i:"
  run_random_script
  echo "-----------------------------------"
done
