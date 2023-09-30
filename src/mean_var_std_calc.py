from typing import List, Dict, Union

import numpy as np


def calculate_mean(grid_arr: List[np.ndarray], flattened_arr: np.ndarray) -> List[Union[List[float], float]]:
    axis0_mean = np.mean(grid_arr, axis=0).tolist()
    axis1_mean = np.mean(grid_arr, axis=1).tolist()
    flattened_mean = np.mean(flattened_arr)

    return [axis0_mean, axis1_mean, flattened_mean]


def calculate_variance(grid_arr: List[np.ndarray], flattened_arr: np.ndarray) -> List[Union[List[float], float]]:
    axis0_variance = np.var(grid_arr, axis=0).tolist()
    axis1_variance = np.var(grid_arr, axis=1).tolist()
    flattened_variance = np.var(flattened_arr)

    return [axis0_variance, axis1_variance, flattened_variance]


def calculate_std_dev(grid_arr: List[np.ndarray], flattened_arr: np.ndarray) -> List[Union[List[float], float]]:
    axis0_std_dev = np.std(grid_arr, axis=0).tolist()
    axis1_std_dev = np.std(grid_arr, axis=1).tolist()
    flattened_std_dev = np.std(flattened_arr)

    return [axis0_std_dev, axis1_std_dev, flattened_std_dev]


def calculate_max(grid_arr: List[np.ndarray], flattened_arr: np.ndarray) -> List[Union[List[float], float]]:
    axis0_max = np.amax(grid_arr, axis=0).tolist()
    axis1_max = np.amax(grid_arr, axis=1).tolist()
    flattened_max = np.amax(flattened_arr)

    return [axis0_max, axis1_max, flattened_max]


def calculate_min(grid_arr: List[np.ndarray], flattened_arr: np.ndarray) -> List[Union[List[float], float]]:
    axis0_min = np.amin(grid_arr, axis=0).tolist()
    axis1_min = np.amin(grid_arr, axis=1).tolist()
    flattened_min = np.amin(flattened_arr)

    return [axis0_min, axis1_min, flattened_min]


def calculate_sum(grid_arr: List[np.ndarray], flattened_arr: np.ndarray) -> List[Union[List[float], float]]:
    axis0_sum = np.sum(grid_arr, axis=0).tolist()
    axis1_sum = np.sum(grid_arr, axis=1).tolist()
    flattened_sum = np.sum(flattened_arr)

    return [axis0_sum, axis1_sum, flattened_sum]


def calculate(array: List[int]) -> Dict[str, List[Union[List[float], float]]]:
    if len(array) < 9:
        raise ValueError("List must contain nine numbers.")

    flattened_arr: np.ndarray = np.array(array)
    grid_arr: List[np.ndarray] = np.array_split(flattened_arr, 3)

    return {
        "mean": calculate_mean(grid_arr, flattened_arr),
        "variance": calculate_variance(grid_arr, flattened_arr),
        "standard deviation": calculate_std_dev(grid_arr, flattened_arr),
        "max": calculate_max(grid_arr, flattened_arr),
        "min": calculate_min(grid_arr, flattened_arr),
        "sum": calculate_sum(grid_arr, flattened_arr),
    }
