from tests import low_capacity_number_of_pages
from tests import different_standard_deviation
from tests import adjusted_capacity_number_of_pages
from tests import high_capacity_number_of_pages

def test_capacity_dependent_on_number_of_pages():
    low_capacity_number_of_pages()
    high_capacity_number_of_pages()
    adjusted_capacity_number_of_pages()


def test_different_standard_deviation():
    different_standard_deviation()


def run_tests():
    test_capacity_dependent_on_number_of_pages()
    test_different_standard_deviation()


run_tests()