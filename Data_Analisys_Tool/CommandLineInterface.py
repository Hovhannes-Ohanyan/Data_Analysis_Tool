from matplotlib import pyplot as plt

from DataSet import DataSet
from DataAnalyzer import DataAnalyzer
from DataVisualization import Visualization

dataset = DataSet()
analyzer = DataAnalyzer(dataset)
visualizer = Visualization(dataset)


def load_data():
    source = input("Enter data source (csv, excel, png): ")
    file_path = input("Enter data file path: ")
    if source == "csv":
        dataset.load_data_from_csv(file_path)
        return "CSV data loaded successfully."
    elif source == "excel":
        sheet_name = input("Enter Excel sheet name: ")
        dataset.load_data_from_excel(file_path, sheet_name)
        return f"Excel data from sheet '{sheet_name}' loaded successfully."
    elif source == "png":
        dataset.load_data_from_png(file_path)
        return "PNG data loaded successfully."
    else:
        return "Invalid data source provided."


def analyze_data():
    column_name = input("Enter the name of the column for analysis: ")
    action = input("Choose the analysis action (mean, std_deviation, median, correlation): ")

    if action == "mean":
        result = analyzer.calculate_mean(column_name)
    elif action == "std_deviation":
        result = analyzer.calculate_standard_deviation(column_name)
    elif action == "median":
        result = analyzer.calculate_median(column_name)
    elif action == "correlation":
        column1 = input("Enter the name of the first column: ")
        column2 = input("Enter the name of the second column: ")
        result = analyzer.calculate_correlation(column1, column2)
    else:
        result = "Invalid analysis action."

    return result


def visualize_data():
    column_names = dataset.get_column_names()
    if not column_names:
        print("No data available. Please load data first.")
        return

    print("Available columns:", column_names)

    plot_type = input("Choose the plot type (histogram, scatter, line): ")
    column_name = input("Enter the name of the column for visualization: ")

    if column_name not in column_names:
        print("Invalid column choice. The column name does not exist.")
        return

    if plot_type == "scatter":
        x_column = input("Enter the name of the x-axis column: ")
        y_column = input("Enter the name of the y-axis column: ")

        if x_column not in column_names or y_column not in column_names:
            print("Error: One or both columns not found")
            return

        plt.scatter(dataset.data[x_column], dataset.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Scatter Plot: {x_column} vs {y_column}")

        plt.show()
        return "Data visualization completed successfully."

    elif plot_type == "histogram":
        data = dataset.data[column_name]
        plt.hist(data, bins=20)
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.title(f"Histogram of {column_name}")

        plt.show()
        return "Data visualization completed successfully."

    elif plot_type == "line":
        x_column = input("Enter the name of the x-axis column: ")
        y_column = input("Enter the name of the y-axis column: ")

        if x_column not in column_names or y_column not in column_names:
            print("Error: One or both columns not found")
            return

        # Line plot
        plt.plot(dataset.data[x_column], dataset.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"Line Plot of {x_column} vs. {y_column}")

        # Show the line plot
        plt.show()
        return "Data visualization completed successfully."

    else:
        return "Invalid plot type."


def main():
    while True:
        print("Choose an action:")
        print("1. Load Data")
        print("2. Analyze Data")
        print("3. Visualize Data")
        print("4. Exit")

        choice = input("Enter the number of the action you want to perform: ")

        if choice == "1":
            print(load_data())
        elif choice == "2":
            print(analyze_data())
        elif choice == "3":
            print(visualize_data())
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
