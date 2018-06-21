
class CompressorUtils(object):
    @staticmethod
    def encode(_cell, _list):
        if not _cell:
            data = "-"
        elif _cell not in _list:
            data = str(len(_list))
            _list.append(_cell)
        else:
            data = str(_list.index(_cell))

        return data

    @staticmethod
    def decode(_cell, _list):
        data = ""
        if _cell is not "-":
            print _cell
            data = _list[int(_cell)]

        return data

    @staticmethod
    def get_lists_string(lists):
        all_lists = ""
        for element in lists:
            all_lists += ','.join(element)
            all_lists += "@"
        return all_lists[:-1]

    @staticmethod
    def get_string_lists(str_to_lists):
        list_of_lists = []
        ll = str_to_lists.split("@")
        for l in ll:
            list_of_lists.append( l.split(","))

        return list_of_lists
