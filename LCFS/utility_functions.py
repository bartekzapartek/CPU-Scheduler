from pathlib import Path
from normal_distribution_generator import normal_distribution
from LCFS_algorithm import Process

# -------------------- Utility Functions --------------------

def save_generated_data_to_file(file_name, burst_times, arrival_times, seed, mean, standard_deviation, sample_size):
    file_path = Path('raw_data') / Path(file_name)
    file_path.parent.mkdir(exist_ok = True, parents = True)

    normal_distribution_info = f'normal_distribution seed={seed} mean={mean} standard_deviation={standard_deviation} sample_size={sample_size}\n'
    data_size = len(burst_times)

    with open(file_path, 'w') as file:
        file.write(normal_distribution_info)
        file.write('-' * 60 + '\n')

        for i in range(0, data_size):
            file.write(f'Burst Time = {burst_times[i]} Arrival Time = {arrival_times[i]}\n')

def save_results_to_file(processes, averages, file_name, seed, mean, standard_deviation, number_of_processes):
    if not file_name:
        return

    path = Path('results') / Path(file_name)
    path.parent.mkdir(exist_ok=True, parents=True)

    process_info = f'# seed={seed} mean={mean} standard_deviation={standard_deviation} number_of_processes={number_of_processes}\n'
    process_info += '-' * 60 + '\n'

    process_info += f'Average waiting time : {averages[0]}\n'
    process_info += f'Average turn around time : {averages[1]}\n'
    process_info += '-' * 60 + '\n'

    for i, process in enumerate(processes):
        process_info += f'Process {i} | Waiting Time {process.waiting_time} | Burst Time {process.burst_time} | Arrival Time {process.arrival_time} | Turn Around Time {process.turn_around_time}\n'




    with open(path, 'w') as file:
        file.write(process_info)

def create_processes(seed, mean, standard_deviation, number_of_processes, file_name=''):
    burst_times = normal_distribution(seed[0], mean[0], standard_deviation[0], number_of_processes)
    arrival_times = normal_distribution(seed[1], mean[1], standard_deviation[1], number_of_processes)

    save_generated_data_to_file(file_name, burst_times, arrival_times, seed, mean, standard_deviation, number_of_processes)

    processes = [Process(burst_times[i], arrival_times[i]) for i in range(0, number_of_processes)]



    return processes


# -------------------- End --------------------
