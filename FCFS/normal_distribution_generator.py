from numpy.random import seed
from numpy.random import normal

def normal_distribution(seed_value, mean, standard_deviation, sample_size):
    seed(seed_value)

    data = normal(loc = mean, scale = standard_deviation, size = sample_size)
    data = [abs(int(x)) for x in data]

    return data
