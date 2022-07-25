class Element:

    def __init__(self, unique_id: int, value: int) -> None:
        self.__unique_id = None
        if isinstance(unique_id, int):
            self.__unique_id = unique_id
        self.__value = None
        if isinstance(value, int):
            self.__value = value
        self.__index_in_archive = None

    @property
    def unique_id(self) -> int:
        return self.__unique_id

    @property
    def value(self) -> int:
        return self.__value

    @property
    def index_in_archive(self) -> int:
        return self.__index_in_archive

    @unique_id.setter
    def unique_id(self, unique_id: int) -> None:
        if isinstance(unique_id, int):
            self.__unique_id = unique_id

    @value.setter
    def value(self, value: int) -> None:
        if isinstance(value, int):
            self.__value = value

    @index_in_archive.setter
    def index_in_archive(self, index_in_archive: int) -> None:
        if isinstance(index_in_archive, int):
            self.__index_in_archive = index_in_archive
