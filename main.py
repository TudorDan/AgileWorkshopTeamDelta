from controller import home_controller
from model import data_manager
import csv


def main():
    print(data_manager.get_table_from_file("students.csv"))
    return

from view import display


print("headers")
if __name__ == '__main__':
    home_controller.menu()
    display.print_nothing
