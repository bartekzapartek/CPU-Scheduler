
class Process:

    def __init__(self, burst_time, arrival_time):
        self.burst_time = burst_time
        self.arrival_time = arrival_time

        self.waiting_time = 0
        self.turn_around_time = 0
        self.service_time = 0
        self.completion_time = 0


def evaluate_completion_time(processes):
    start_time = 0

    for i in range(len(processes)):
        if start_time < processes[i].arrival_time:
            start_time = processes[i].arrival_time

        start_time = start_time + processes[i].burst_time

        end_time = start_time
        processes[i].completion_time = end_time

def evaluate_waiting_time(processes):

    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i].turn_around_time - processes[i].burst_time

def evaluate_turn_around_time(processes):
    for process in processes:
        process.turn_around_time = process.completion_time - process.arrival_time

def lcfs(processes):
    total_waiting_time = 0
    total_turn_around_time = 0

    processes = sorted(processes, key = lambda x: x.arrival_time, reverse = True)

    evaluate_completion_time(processes)
    evaluate_turn_around_time(processes)
    evaluate_waiting_time(processes)

    for i, process in enumerate(processes):
        total_waiting_time += process.waiting_time
        total_turn_around_time += process.turn_around_time

    return processes, total_waiting_time, total_turn_around_time






