from pathlib import Path
from normal_distribution_generator import normal_distribution

def save_raw_data_to_file(pages, file_name, normal_distribution_info):
    if not file_name:
        return
    file_path = Path('raw_data') / Path(file_name)
    file_path.parent.mkdir(exist_ok=True, parents=True)

    header = process_info = f'# seed={normal_distribution_info[0]} mean={normal_distribution_info[1]} standard_deviation={normal_distribution_info[2]} number_of_pages={normal_distribution_info[3]}\n'
    header += '-' * 60 + '\n'

    with open(file_path, 'w') as file:
        file.write(header)

        for page in pages:
            file.write(str(page) + '\n')


def save_results_to_file(pages, page_faults, lru_cache_status, file_name, normal_distribution_info, capacity):
    if not file_name:
        return

    file_path = Path('results') / Path(file_name)
    file_path.parent.mkdir(exist_ok=True, parents=True)

    header = process_info = f'# seed = {normal_distribution_info[0]} mean = {normal_distribution_info[1]} standard_deviation = {normal_distribution_info[2]} number_of_pages = {normal_distribution_info[3]}\n'
    header += f'Capacity of LSU = {capacity}\n'
    header += '-' * 60 + '\n'

    page_faults_info = f'Page Faults = {page_faults}\n'
    page_faults_info += f'Page Hits = {normal_distribution_info[3] - page_faults}\n'
    page_faults_info += '-' * 60 + '\n'

    changes_of_cache = ''


    for i, pages_cached in enumerate(lru_cache_status):
        if pages_cached[-1] == 'page_fault':
            pages_cached.pop(-1)
            changes_of_cache += str(pages_cached) + f' <-- Page - {pages[i]} | Page Fault Here\n'
        else:
            changes_of_cache += str(pages_cached) + f' <-- Page - {pages[i]}\n'


    changes_of_cache += '-' * 60 + '\n'

    with open(file_path, 'w') as file:
        file.write(header)
        file.write(page_faults_info)
        file.write(changes_of_cache)



def generate_pages(seed, mean, standard_deviation, number_of_pages, file_name = ''):
    pages = normal_distribution(seed, mean, standard_deviation, number_of_pages)

    save_raw_data_to_file(pages, file_name, (seed, mean, standard_deviation, number_of_pages))

    return pages
