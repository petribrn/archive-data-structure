class SearchIndexHelper:
    """
        Probably best way to implement ordered indexes here is
        by using doubly linked list that had already been implemented.
    """
    def __init__(self) -> None:
        self.__indexed_elements = []

    def add_new_element(self, unique_id: int, index_in_archive: int) -> None:
        self.__indexed_elements.append([index_in_archive, unique_id])

        # Sort the dict by unique_id
        self.__indexed_elements = sorted(self.__indexed_elements, key= lambda x: x[1])

    def remove_element(self, unique_id: int) -> None:
        indexed_element = self.search_element(unique_id)
        if indexed_element:
            self.__indexed_elements.pop(self.__indexed_elements.index(indexed_element))

            # Sort the dict by unique_id
            self.__indexed_elements = sorted(self.__indexed_elements, key= lambda x: x[1])
        else:
            raise ValueError("Failed to remove element: There's no element with the ID searched.")

    def search_element(self, unique_id: int) -> list:
        for indexed_element in self.__indexed_elements:
            if indexed_element[1] == unique_id:
                #      [  index_archive     ,   unique_id     ]
                return [indexed_element[0], indexed_element[1]]
        return False

    @property
    def indexed_elements(self) -> dict:
        return self.__indexed_elements
