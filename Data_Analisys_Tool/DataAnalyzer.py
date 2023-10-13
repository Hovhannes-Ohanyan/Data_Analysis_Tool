import numpy as np

from scipy.stats import stats


class DataAnalyzer:
    def __init__(self, dataset):
        self.dataset = dataset

    def calculate_mean(self, column_name):
        if self.dataset is not None:
            try:
                column = self.dataset.data[column_name]
                # Check if the column contains numeric data
                if np.issubdtype(column.dtype, np.number):
                    mean_value = np.mean(column)
                    return mean_value
                else:
                    return "Error: Column '{column_name}' does not contain numeric data."
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset Provided"

    def calculate_standard_deviation(self, column_name):
        """
            Calculate the standard deviation of a specified column in the dataset.
            Args:
                column_name (str): The name of the column for which to calculate the standard deviation.
        """
        if self.dataset is not None:
            try:
                std_deviation = np.std(self.dataset.data[column_name])
                return std_deviation
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset Provided"

    def calculate_median(self, column_name):
        if self.dataset is not None:
            try:
                column = self.dataset.data[column_name]
                # Check if the column contains numeric data
                if np.issubdtype(column.dtype, np.number):
                    median_value = np.median(column)
                    return median_value
                else:
                    return "Error: Column '{column_name}' does not contain numeric data."
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset Provided"

    def calculate_correlation(self, column1, column2):
        """
            Calculate the correlation between two columns in the dataset.
            Args:
                column1 (str): The name of the first column.
                column2 (str): The name of the second column.
        """
        if self.dataset is not None:
            try:
                correlation = np.corrcoef(self.dataset.data[column1], self.dataset.data[column2])[0, 1]
                return correlation

            except KeyError:
                print(f"Error: One or both columns not found")
        else:
            return "Error: No dataset provided"

    def calculate_variance(self, column_name):
        """
            Calculate the variance of a specified column in the dataset
            Args:
                column_name (str) : The name of the column for which to calculate the variance
        """

        if self.dataset is not None:
            try:
                variance_value = np.var(self.dataset.data[column_name])
                return variance_value
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No database provided"

    def calculate_quartiles(self, column_name):
        """
            Calculate the quartiles (25,th,50th, and 75th percentiles) of specified column in the dataset
            Args:
                column_name (str): The name of the column for which to calculate the quartiles.
        """
        if self.dataset is not None:
            try:
                quartiles = np.percentile(self.dataset.data[column_name], [25, 50, 75])
                return quartiles
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset provided"

    def calculate_mode(self, column_name):
        """
            Calculate the mode of a specified column in the dataset.
            Args:
                column_name (str): The name of the column for which to calculate the mode.
        """
        if self.dataset is not None:
            try:
                mode_value = self.dataset.data[column_name].mode()[0]
                return mode_value
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset provided"

    def log_transform(self, column_name):
        """
            Apply a natural logarithm (log) transformation to a specified column.
            Args:
                column_name (str): The name of the column to transform.
        """
        if self.dataset is not None:
            try:
                self.dataset.data[column_name] = np.log(self.dataset.data[column_name])
                print(f"Log-transformed '{column_name}' column")
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        return "Error: No dataset provided"

    def calculate_log_sum(self, column_name):
        """
            Calculate the sum of logarithms  of values in a specified column
            Args:
                column_name (str) : The name of the column
        """
        if self.dataset is not None:
            try:
                log_sum = np.sum(np.log(self.dataset.data[column_name]))
                return log_sum
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset provided"

    def calculate_geometric_mean(self, column_name):
        """
            Calculate the geometric mean of a specified column in the dataset
            Args:
            column_name (str): The name of the column for which to calculate the geometric mean
        """
        if self.dataset is not None:
            try:
                geometric_mean = stats.gmean(self.dataset.data[column_name])
                return geometric_mean
            except KeyError:
                print(f"Error: Column '{column_name}' not found")
        else:
            return "Error: No dataset provided"
