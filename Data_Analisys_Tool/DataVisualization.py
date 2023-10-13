import matplotlib.pyplot as plt
import seaborn as sns


class Visualization:
    def __init__(self, dataset):
        self.dataset = dataset

    def plot_histogram(self, column_name):
        """
            Create a histogram plot for a specified column in the dataset
            Args:
                column_name (str): The name of the column to plot
        """
        if self.dataset is not None:
            try:
                data = self.dataset.data[column_name]
                plt.hist(data, bins=20, edgecolor='k')
                plt.xlabel(column_name)
                plt.ylabel("Frequency")
                plt.title(f"Histogram of {column_name}")
                plt.show()
            except KeyError:
                print(f"Error: Column '{column_name}' not found ")
        else:
            print("Error: No dataset provided")

    def scatter_plot(self, x_column, y_column):
        """
            Create a scatter plot for two columns in the dataset
            Args:
                x_column (str) : The name of the x-axis column
                y_column (str) : The name of the y-axis column
        """

        if self.dataset is not None:
            try:
                plt.scatter(self.dataset.data[x_column], self.dataset.data[y_column])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f'Scatter Plot: {x_column} vs. {y_column}')
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
        else:
            print("Error: No dataset provided")

    def line_plot(self, x_column, y_column):
        """
            Create a line plot for two columns in the dataset
            Args:
                x_column (str) : The name of the x-axis column
                y_column (str) : The name of the y-axis column

        """
        if self.dataset is not None:
            try:
                plt.plot(self.dataset.data[x_column], self.dataset.data[y_column])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f"Line Plot : {y_column} over {x_column}")
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
        else:
            print("Error: No dataset provided")

    def bar_chart(self, x_column, y_column):
        """
            Create a bar chart for two columns in the dataset.
            Args:
                x_column (str): The name of the x-axis column (categorical).
                y_column (str): The name of the y-axis column (numeric).
        """

        if self.dataset is not None:
            try:
                sns.barplot(x=self.dataset.data[x_column], y=self.dataset.data[y_column])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f'Bar Chart: {y_column} by {x_column}')
                plt.xticks(rotation=45)
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
        else:
            print("Error: No dataset provided")

    def pie_chart(self, column_name):
        """
            Create a pie chart to visualize the distribution of categories in a column.
            Args:
                column_name (str): The name of the column with categorical data.
        """
        if self.dataset is not None:
            try:
                counts = self.dataset.data[column_name].value_counts()
                plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=140)
                plt.axis("equal")
                plt.title(f"Pie Chart: {column_name} Distribution")
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
        else:
            print("Error: No dataset provided")

    def heatmap(self):
        """
            Create a heatmap to visualize the correlation matrix of numeric data.
            Heatmaps are useful for identifying patterns in data.
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                correlation_matrix = self.dataset.data.corr()
                sns.heatmap(correlation_matrix, annot=True, cmap="cool-warm", linewidths=0.5)
                plt.title("Correlation Heatmap")
                plt.show()
            except Exception as e:
                print(f"Error creating heatmap: {str(e)}")
        else:
            print("Error: No dataset provided.")

    def pair_plot(self, columns):
        """
            Create pair plots (scatter matrix) for multiple numeric columns to visualize pairwise
            relationships in the data.
            Args:
                columns (list of str): List of column names to include in the pair plot.
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                sns.palplot(self.dataset.data[columns])
                plt.title('Pair Plot')
                plt.show()
            except Exception as e:
                print(f"Error creating heatmap: {str(e)}")
        else:
            print("Error: No dataset provided.")

    def violin_plot(self, x_column, y_column):
        """
            Create a violin plot to visualize the distribution of data similar to box plots
            but with a rotated kernel density plot on each side.
            Args:
                x_column (str): The name of the x-axis column (categorical).
                y_column (str): The name of the y-axis column (numeric).
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                sns.violinplot(x=self.dataset.data[x_column], y=self.dataset.data[y_column])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f"Violin Plot: {y_column} by {x_column}")
                plt.xticks(rotation=45)
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
            except Exception as e:
                print(f"Error creating violin plot: {str(e)}")
        else:
            print("Error: No dataset provided")

    def density_plot(self, column_name):
        """
            Create a density plot (kernel density estimate) to visualize the probability density function
            of a numeric variable.
            Args:
                column_name (str): The name of the column to visualize.
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                sns.kdeplot(self.dataset.data[column_name], shade=True)
                plt.xlabel(column_name)
                plt.title(f"Density Plot: {column_name}")
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
            except Exception as e:
                print(f"Error creating violin plot: {str(e)}")
        else:
            print("Error: No dataset provided")

    def bar_plot(self, x_column, y_column, hue_column=None, stacked=False):
        """
            Create a bar plot to compare categories across multiple subgroups.
            Args:
                x_column (str): The name of the x-axis column (categorical).
                y_column (str): The name of the y-axis column (numeric).
                hue_column (str, optional): The name of the column to group by (categorical).
                stacked (bool): If True, create a stacked bar plot; if False, create a grouped bar plot.
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                if hue_column:
                    sns.barplot(data=self.dataset.data, x=x_column, y=y_column, hue=hue_column)
                else:
                    sns.barplot(data=self.dataset.data, x=x_column, y=y_column)
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f"Bar Plot: {y_column} by {x_column}")
                if stacked:
                    plt.legend(title=hue_column)
                plt.xticks(rotation=45)
                plt.show()
            except KeyError:
                print(f"Error: One or both columns not found")
            except Exception as e:
                print(f"Error creating violin plot: {str(e)}")
        else:
            print("Error: No dataset provided")

    def time_series_plot(self, x_column, y_column):
        """
            Visualize time series data with specific attention to trends, seasonality, and anomalies.
            Args:
                x_column (str): The name of the x-axis column (usually time or date).
                y_column (str): The name of the y-axis column (numeric).
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                plt.plot(self.dataset.data[x_column], self.dataset.data[y_column])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f"Time Series Plot: {y_column} over {x_column}")
                plt.xticks(rotation=45)
                plt.show()

            except KeyError:
                print(f"Error: One or both columns not found")
            except Exception as e:
                print(f"Error creating violin plot: {str(e)}")
        else:
            print("Error: No dataset provided")

    def scatter_3d_plot(self, x_column, y_column, z_column):
        """
            Create a 3D scatter plot for three-dimensional data visualization.
            Args:
                x_column (str): The name of the x-axis column.
                y_column (str): The name of the y-axis column.
                z_column (str): The name of the z-axis column.
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(self.dataset.data[x_column], self.dataset.data[y_column], self.dataset.data[z_column])
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                ax.set_zlabel(z_column)
                plt.title(f'3D Scatter Plot: {x_column} vs. {y_column} vs. {z_column}')
            except KeyError:
                print(f"Error: One or both columns not found")
            except Exception as e:
                print(f"Error creating violin plot: {str(e)}")
        else:
            print("Error: No dataset provided")

    def pairwise_scatter_matrix(self, columns):
        """
            Create a grid of scatter plots for pairwise relationships between columns.
            Args:
                columns (list of str): List of column names to include in the scatter matrix.
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                sns.palplot(self.dataset.data[columns])
                plt.title("Pairwise Scatter Matrix")
                plt.show()
            except KeyError:
                print("Error: One or more columns not found")
            except Exception as e:
                print(f"Error creating pairwise scatter matrix: {str(e)}")
        else:
            print(f"Error: No dataset provided")

    def boxen_plot(self, x_column, y_column):
        """
            Create a boxen plot to visualize the distribution of data.
            Args:
                x_column (str): The name of the x-axis column (categorical).
                y_column (str): The name of the y-axis column (numeric).
        """
        if self.dataset is not None and self.dataset.data is not None:
            try:
                sns.boxenplot(x=self.dataset.data[x_column], y=self.dataset.data[y_column])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f"Boxen Plot: {y_column} by {x_column}")
                plt.show()
            except KeyError:
                print("Error: One or more columns not found")
            except Exception as e:
                print(f"Error creating pairwise scatter matrix: {str(e)}")
        else:
            print(f"Error: No dataset provided")
