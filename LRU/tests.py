from LRU_algorithm import LRU
from utility_functions import generate_pages, save_results_to_file


def different_standard_deviation():
    SEED = 1
    MEAN = 50
    STANDARD_DEVIATION = [1, 3, 10, 30, 75, 100, 300, 500, 750]

    CAPACITY = 90
    NUMBER_OF_PAGES = 300

    DIR_NAME = 'different_standard_deviation'

    for standard_deviation in STANDARD_DEVIATION:
        pages = generate_pages(SEED, MEAN, standard_deviation, NUMBER_OF_PAGES,  f'{DIR_NAME}/{SEED}s.{MEAN}m.{standard_deviation}std.{NUMBER_OF_PAGES}nof.{CAPACITY}cap.txt')
        lru = LRU(capacity = CAPACITY, pages = [])

        lru_cache_status = []

        for page in pages:
            was_page_fault = lru.check_page_in_cache(page)
            lru_cache_status.append(list(lru.pages))

            if was_page_fault:
                lru_cache_status[-1].append('page_fault')


        save_results_to_file(pages, lru.page_faults, lru_cache_status,
                             f'{DIR_NAME}/{SEED}s.{MEAN}m.{standard_deviation}std.{NUMBER_OF_PAGES}nof.{CAPACITY}cap.txt',
                             (SEED, MEAN, standard_deviation, NUMBER_OF_PAGES), CAPACITY)


# -------------------------------

def low_capacity_number_of_pages():
    SEED = 1
    MEAN = 50
    STANDARD_DEVIATION = 10

    CAPACITY = 5
    NUMBER_OF_PAGES = [10, 100, 250, 500, 1000]

    DIR_NAME = 'low_capacity_number_of_pages'

    for pages_count in NUMBER_OF_PAGES:
        pages = generate_pages(SEED, MEAN, STANDARD_DEVIATION, pages_count, f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{pages_count}nop.{CAPACITY}cap.txt')
        lru = LRU(capacity = CAPACITY, pages = [])

        lru_cache_status = []

        for page in pages:
            was_page_fault = lru.check_page_in_cache(page)
            lru_cache_status.append(list(lru.pages))

            if was_page_fault:
                lru_cache_status[-1].append('page_fault')

        save_results_to_file(pages, lru.page_faults, lru_cache_status,
                             f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{pages_count}nop.{CAPACITY}cap.txt',
                             (SEED, MEAN, STANDARD_DEVIATION, pages_count), CAPACITY)



def adjusted_capacity_number_of_pages():
    SEED = 1
    MEAN = 50
    STANDARD_DEVIATION = 10

    #CAPACITY = [5, 50, 125, 250, 500]
    CAPACITY = [2, 25, 72, 125, 250]
    NUMBER_OF_PAGES = [10, 100, 250, 500, 1000]

    DIR_NAME = 'adjusted_capacity_number_of_pages'

    for i in range(len(NUMBER_OF_PAGES)):
        pages = generate_pages(SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i], f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt')
        lru = LRU(capacity = CAPACITY[i], pages = [])

        lru_cache_status = []

        for page in pages:
            was_page_fault = lru.check_page_in_cache(page)
            lru_cache_status.append(list(lru.pages))

            if was_page_fault:
                lru_cache_status[-1].append('page_fault')

        save_results_to_file(pages, lru.page_faults, lru_cache_status,
                             f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt',
                             (SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i]), CAPACITY[i])

def adjusted_capacity_number_of_pages():
    SEED = 1
    MEAN = 50
    STANDARD_DEVIATION = 10

    CAPACITY = [5, 50, 125, 250, 500]
    NUMBER_OF_PAGES = [10, 100, 250, 500, 1000]

    DIR_NAME = 'adjusted_capacity_number_of_pages'

    for i in range(len(NUMBER_OF_PAGES)):
        pages = generate_pages(SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i], f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt')
        lru = LRU(capacity = CAPACITY[i], pages = [])

        lru_cache_status = []

        for page in pages:
            was_page_fault = lru.check_page_in_cache(page)
            lru_cache_status.append(list(lru.pages))

            if was_page_fault:
                lru_cache_status[-1].append('page_fault')

        save_results_to_file(pages, lru.page_faults, lru_cache_status,
                             f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt',
                             (SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i]), CAPACITY[i])

    SEED = 1
    MEAN = 50
    STANDARD_DEVIATION = 10

    CAPACITY = [2, 25, 62, 125, 250]
    NUMBER_OF_PAGES = [10, 100, 250, 500, 1000]

    DIR_NAME = 'adjusted_capacity_number_of_pages'

    for i in range(len(NUMBER_OF_PAGES)):
        pages = generate_pages(SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i],
                               f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt')
        lru = LRU(capacity=CAPACITY[i], pages=[])

        lru_cache_status = []

        for page in pages:
            was_page_fault = lru.check_page_in_cache(page)
            lru_cache_status.append(list(lru.pages))

            if was_page_fault:
                lru_cache_status[-1].append('page_fault')

        save_results_to_file(pages, lru.page_faults, lru_cache_status,
                             f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt',
                             (SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i]), CAPACITY[i])



def high_capacity_number_of_pages():
    SEED = 1
    MEAN = 50
    STANDARD_DEVIATION = 10

    CAPACITY = [15, 150, 300, 550, 1050]
    NUMBER_OF_PAGES = [10, 100, 250, 500, 1000]

    DIR_NAME = 'high_capacity_number_of_pages'

    for i in range(len(NUMBER_OF_PAGES)):
        pages = generate_pages(SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i], f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt')
        lru = LRU(capacity = CAPACITY[i], pages = [])

        lru_cache_status = []

        for page in pages:
            was_page_fault = lru.check_page_in_cache(page)
            lru_cache_status.append(list(lru.pages))

            if was_page_fault:
                lru_cache_status[-1].append('page_fault')

        save_results_to_file(pages, lru.page_faults, lru_cache_status,
                             f'{DIR_NAME}/{SEED}s.{MEAN}m.{STANDARD_DEVIATION}std.{NUMBER_OF_PAGES[i]}nof.{CAPACITY[i]}cap.txt',
                             (SEED, MEAN, STANDARD_DEVIATION, NUMBER_OF_PAGES[i]), CAPACITY[i])


