# This entrypoint file to be used in development. Start by reading README.md
from src import mean_var_std_calc
from unittest import main

print(mean_var_std_calc.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Run unit tests automatically
main(module='tests.test_module', exit=False)
