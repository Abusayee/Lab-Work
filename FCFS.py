print(" implementalgorithms of FCFS")
def find_waiting_time(processes, n, burst_time, waiting_time):

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

def find_turn_around_time(processes, n, burst_time, waiting_time, turn_around_time):

    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]

def find_avg_time(processes, n, burst_time):
    waiting_time = [0] * n
    turn_around_time = [0] * n

    
    find_waiting_time(processes, n, burst_time, waiting_time)

    find_turn_around_time(processes, n, burst_time, waiting_time, turn_around_time)

    print("Processes    Burst Time    Waiting Time    Turn-Around Time")
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turn_around_time += turn_around_time[i]
        print(f"  {processes[i]} \t\t {burst_time[i]} \t\t {waiting_time[i]} \t\t {turn_around_time[i]}")

    avg_waiting_time = total_waiting_time / n
    avg_turn_around_time = total_turn_around_time / n
    print(f"\nAverage Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turn-Around Time = {avg_turn_around_time:.2f}")


if __name__ == "__main__":

    processes = [1, 2, 3, 4]
    n = len(processes)

    burst_time = [21, 3, 6, 2]
    find_avg_time(processes, n, burst_time)
