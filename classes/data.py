import pandas as pd
import numpy as np

class Variable:

    def __init__(self, var_name, path, batch_names):
        """A class to represent de data obtein by the concilliation"""
        self.name = var_name
        self.filename = path
        self.batch_names = batch_names
        self.number_of_batches = len(batch_names)
        self.batches = self.get_batch_values()
        return

    def get_batch_values(self):
        """Get the data from the excel"""
        batches = {}
        for batch in self.batch_names:
            batches[batch] = pd.read_excel(self.filename,
                                           sheet_name=self.batch_names[batch],
                                           usecols='B').values
        return batches
