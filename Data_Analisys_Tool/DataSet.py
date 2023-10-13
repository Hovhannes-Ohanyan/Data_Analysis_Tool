import os
import pandas as pd
import pytesseract
from PIL import Image


class DataSet:
    def __init__(self):
        self.data = None
        self.metadata = {}

    def load_data_from_csv(self, file_path: str):
        """
        Load data from a CSV file
        Args:
            file_path (str): The path to the CSV file.
        """
        try:
            self.data = pd.read_csv(file_path)
            self.metadata["source"] = "CSV"
            return self.data

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
        except Exception as e:
            print(f"Error loading data from CSV : {str(e)}")

    def load_data_from_excel(self, file_path: str, sheet_name: str):
        """
        Load data from an  Excel file
        Args:
            file_path (str): The path to the Excel file.
            sheet_name (str): The name of the sheet to load.
        """

        try:
            self.data = pd.read_excel(file_path, sheet_name=sheet_name)
            self.metadata["source"] = "Excel"
            return self.data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
        except Exception as e:
            print(f"Error loading data from Excel : {str(e)} ")

    def load_data_from_png(self, image_path):
        """
           Load data from a PNG image
           Args:
               image_path (str): The path to the PNG image.
        """
        try:
            image = Image.open(image_path)
            text_data = pytesseract.image_to_data(image)
            data = [line.split('\t') for line in text_data.split('\n')]
            df = pd.DataFrame(data[1:], columns=data[0])
            self.data = df
            self.metadata["source"] = "PNG"
            return self.data
        except FileNotFoundError:
            print(f"Error: File '{image_path}' not found")
        except Exception as e:
            print(f"Error loading data from PNG : {str(e)}")

    @staticmethod
    def list_files(directory_path):
        """
            List files in a directory.
            Args:
                directory_path (str): The path to the directory.
        """
        try:
            files = os.listdir(directory_path)
            return files
        except FileNotFoundError:
            print(f"Error: Directory '{directory_path}' not found")
            return []
        except Exception as e:
            print(f"Error listing files: {str(e)}")

    def get_column_names(self):
        if self.data is not None:
            return self.data.columns.tolist()
        else:
            return []
