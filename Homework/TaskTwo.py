import csv
import pickle


class CsvPicklizer:
    def __read_csv(self, csv_path):
        result = ""
        with open(csv_path, "r", encoding="utf-8") as csv_in:
            csv_reader = csv.reader(csv_in)
            for i in [i for i in csv_reader if len(i) > 0]:
                result += "".join(i)
        return result

    def __print_pickle_string(self, csv_path):
        data = self.__read_csv(csv_path)
        pickle_string = pickle.dumps(data)
        print(pickle_string)

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.__print_pickle_string(csv_path)


csv_path = r"./test_input.csv"

reader = CsvPicklizer(csv_path)
