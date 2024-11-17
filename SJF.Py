print( "sort job first algorithms")
def find_waiting_time(processes, n, burst_time, waiting_time):
    completed_time = [0] * n
    waiting_time[0] = 0  

    for i in range(1, n):
        completed_time[i - 1] = burst_time[i - 1] + waiting_time[i - 1]
        waiting_time[i] = completed_time[i - 1]

def find_turn_around_time(processes, n, burst_time, waiting_time, turn_around_time):
    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]

def find_avg_time(processes, n, burst_time):
    waiting_time = [0] * n
    turn_around_time = [0] * n
    find_waiting_time(processes, n, burst_time, waiting_time)
    find_turn_around_time(processes, n, burst_time, waiting_time, turn_around_time)

 
    print(f"{'Processes':<10}{'Burst Time':<12}{'Waiting Time':<15}{'Turn-Around Time'}")
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turn_around_time += turn_around_time[i]
        print(f"{processes[i]:<10}{burst_time[i]:<12}{waiting_time[i]:<15}{turn_around_time[i]}")

    
    avg_waiting_time = total_waiting_time / n
    avg_turn_around_time = total_turn_around_time / n
    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turn-Around Time = {avg_turn_around_time:.2f}")

def sort_processes_by_burst_time(processes, burst_time):
    n = len(processes)
    for i in range(n):
        for j in range(i + 1, n):
            if burst_time[i] > burst_time[j]:
                # Swap burst times
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                # Swap process IDs
                processes[i], processes[j] = processes[j], processes[i]

# Main code
if __name__ == "__main__":
   
    processes = [1, 2, 3, 4,5]
    n = len(processes)

    burst_time = [6, 8, 7, 3,7]

    sort_processes_by_burst_time(processes, burst_time)

    find_avg_time(processes, n, burst_time)
