def job_sequencing(jobs):
    # Sort jobs based on descending profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline to determine the number of time slots
    max_deadline = max(job[1] for job in jobs)

    # Initialize time slots and total profit
    time_slots = [-1] * max_deadline
    total_profit = 0

    # Iterate through each job
    for job in jobs:
        job_id, deadline, profit = job

        # Find a free time slot for this job (starting from the last possible slot)
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if time_slots[slot] == -1:
                time_slots[slot] = job_id
                total_profit += profit
                break

    # Filter out unassigned slots and prepare the job sequence
    job_sequence = [job_id for job_id in time_slots if job_id != -1]

    return job_sequence, total_profit

# Function to get user input
def get_user_input():
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))
    for _ in range(num_jobs):
        job_id = input("Enter Job ID: ")
        deadline = int(input(f"Enter deadline for job {job_id}: "))
        profit = int(input(f"Enter profit for job {job_id}: "))
        jobs.append((job_id, deadline, profit))
    return jobs

# Main function
def main():
    jobs = get_user_input()
    sequence, profit = job_sequencing(jobs)
    print(f"\nOptimal job sequence: {sequence}")
    print(f"Total profit: {profit}")

if __name__ == "__main__":
    main()
