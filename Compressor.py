import csv
from utils import CompressorUtils as Utils


class Compressor(object):

    def __init__(self, _file_path, _n_columns=4, _delimiter=","):
        self.file_path = _file_path
        self.txt_file = _file_path.replace("csv", "txt")
        self.n_columns = _n_columns
        self.delimiter = _delimiter
        # lists to hold the values of the table column1_list, column2_list etc.
        self.lists = [[] for _ in xrange(self.n_columns)]

    def compress(self):
        # file to hold the encoded data
        new_file = ""
        with open(self.file_path, 'rb') as csv_file:
            file_reader = csv.reader(csv_file, delimiter=self.delimiter)

            for row in file_reader:
                # mark the start of a new row
                new_file += "&"
                # sort the cells into the right lists
                for i in xrange(self.n_columns):
                    new_file += Utils.encode(row[i].strip(), self.lists[i]) + "'"

        # write the compressed file
        with open(self.txt_file, "w") as text_file:
            text_file.writelines(Utils.get_lists_string(self.lists))
            text_file.writelines("@@@")
            text_file.write(new_file[:-1])

    def decompress(self, _file_path):
        # read from the compressed file
        with open(self.txt_file, "r") as text_file:
            txt = text_file.read()

        lists, encoded_data = txt.split("@@@")
        list_of_lists = Utils.get_string_lists(lists)
        with open(_file_path, 'wb') as csv_file:
            rows = encoded_data.split("&")
            for row in rows:
                if not row:
                    continue

                new_line = ""
                cells = row.split("'")
                # decode the data
                for i in xrange(self.n_columns):
                    new_line += Utils.decode(cells[i], list_of_lists[i]) + ","

                # write to the new csv file
                csv_file.write(new_line[:-1])
                csv_file.write('\n')
