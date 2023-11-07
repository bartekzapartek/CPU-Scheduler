from FCFS_algorithm import fcfs
from utility_functions import create_processes
from utility_functions import save_results_to_file



def test_low_burst_time():
    SEED = (1, 2)
    MEAN = (5, 20)
    STANDARD_DEVIATION = (1, 15)
    NUMBER_OF_PROCESSES = [10, 100, 500, 1000]

    for sample_size in NUMBER_OF_PROCESSES:
        file_name_raw = f'low_burst_time/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{sample_size}nop.txt'

        processes = create_processes(SEED, MEAN, STANDARD_DEVIATION, sample_size, file_name = file_name_raw)
        processes, total_waiting_time, total_turn_around_time = fcfs(processes)

        average_waiting_time = total_waiting_time / sample_size
        average_turn_around_time = total_turn_around_time / sample_size

        file_name_results = f'low_burst_time/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{sample_size}nop.txt'
        save_results_to_file(processes, (average_waiting_time, average_turn_around_time), file_name_results, SEED, MEAN, STANDARD_DEVIATION, sample_size)

def test_medium_burst_time():
    SEED = (1, 2)
    MEAN = (250, 20)
    STANDARD_DEVIATION = (50, 15)
    NUMBER_OF_PROCESSES = [10, 100, 500, 1000]

    for sample_size in NUMBER_OF_PROCESSES:
        file_name_raw = f'medium_burst_time/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{sample_size}nop.txt'

        processes = create_processes(SEED, MEAN, STANDARD_DEVIATION, sample_size, file_name = file_name_raw)
        processes, total_waiting_time, total_turn_around_time = fcfs(processes)

        average_waiting_time = total_waiting_time / sample_size
        average_turn_around_time = total_turn_around_time / sample_size

        file_name_results = f'medium_burst_time/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{sample_size}nop.txt'
        save_results_to_file(processes, (average_waiting_time, average_turn_around_time), file_name_results, SEED, MEAN, STANDARD_DEVIATION, sample_size)




