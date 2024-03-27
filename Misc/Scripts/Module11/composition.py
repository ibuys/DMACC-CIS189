"""
CIS189 Module 11 Composition assignment script.
"""
import random


# Do not modify.
class Memory:
    """
    Class representation of computer memory.
    """
    def __init__(self):

        self.total_ram_gb = 16

    def available(self):
        in_use = random.uniform(0, self.total_ram_gb)
        avail = self.total_ram_gb - in_use 
        return avail


# Do not modify.
class DiskSpace:
    """
    Class representation of computer hard disk storage.
    """
    def __init__(self):
        self.total_capacity_gb = 512

    def available(self):
        in_use = random.uniform(0, self.total_capacity_gb)
        avail = self.total_capacity_gb - in_use 
        return avail



class Computer:
    """
    Computer class. 
    
    Attributes:
        name: str
            Passed in as an argument to the constructor. 

    Methods: 
        get_info:
            Returns a string of the form:

            [timestamp] computer name: <name>, available memory: <available memory>, available storage: <available storage>
    
    """

    # Remove pass after you add your code.

    ##### YOUR CODE HERE #####
    pass




def main():


    machine_names = ["RQS445", "MIKES-MACHINE", "Leet-315"]

    # For each of the machine_names, create an instance of the Computer
    # class, then call `get_info` for each. 

    ##### YOUR CODE HERE #####
