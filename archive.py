from multiprocessing.sharedctypes import Value
from search_index_helper import SearchIndexHelper
from empty_positions import EmptyPositionArray
from element import Element

class Archive:
    """
     Fixed size archive data structure
    """
    def __init__(self, archive_size: int) -> None:
        if isinstance(archive_size, int): 
            self.__archive_size = archive_size
        else:
            raise ValueError('Unsuported type for archive size. Please enter a number.')
        self.__empty_positions = EmptyPositionArray(archive_size)
        self.__search_index_helper = SearchIndexHelper()
        self.__archive = ["Empty"] * archive_size if isinstance(archive_size, int) else None

    def insert_new_element(self, unique_id: int, value: int) -> None:
        try:
            if not (isinstance(unique_id, int) and isinstance(value, int)):
                raise ValueError("Usuported type for this parameters. Please enter a number.")
            if self.__search_index_helper.search_element(unique_id):
                raise ValueError("This ID has been already used. Try a different one.")
                
            element = Element(unique_id, value) # Creates new Element instance

            if len(self.__empty_positions.array) != 0:
                # Gets first empty position index and allocate new element into it.
                index = self.__empty_positions.use_empty_position()
                self.__archive[index] = element
            else:
                raise ValueError('Archive is full, you must remove an element before inserting a new one.')

            # Sets index of element
            element.index_in_archive = self.__archive.index(element)

            # Updates indexed_elements object with the new element's id and index in archive
            self.__search_index_helper.add_new_element(element.unique_id, element.index_in_archive)

        except Exception as e:
            print(e)

    def remove_element(self, unique_id: int):
        """
        remove_element _summary_

        Removes a specific element based on given unique_id from archive.

        Basically:
        -> Removes element from index structure (search_index_helper);
        -> Tags back an "Empty" position to where the element was located;
        -> Adds element past location as a new empty position into empty_positions array.

        Args:
            unique_id (int): to be removed element's unique id
        """
        try:
            if not isinstance(unique_id, int):
                raise ValueError("Usuported type for this parameters. Please enter a number.")
                
            # Search for element in indexed list and remove it
            indexed_element = self.search_element(unique_id)
            self.__search_index_helper.remove_element(unique_id)

            # Set element archive's index value to "Empty"
            self.__archive[indexed_element[0]] = "Empty"

            # Updates empty_positions array with the new empty position (index)
            self.__empty_positions.add_empty_position(indexed_element[0])
        except Exception as e:
            print(e)

    def search_element(self, unique_id: int) -> list:
        try: 
            if not isinstance(unique_id, int):
                    raise ValueError("Usuported type for this parameters. Please enter a number.")

            indexed_element = self.__search_index_helper.search_element(unique_id)
            if not indexed_element:
                raise ValueError("There's no element with the ID searched.")
            return indexed_element
        except Exception as e:
            print(e)

    def list_ordered_elements(self) -> None:
        indexed_elements = self.__search_index_helper.indexed_elements # Already ordered list of elements
        empty_positions = self.__empty_positions.array
        printable_list = ["free_space"] * self.__archive_size 
        if len(indexed_elements) > 0:
            # Add the value to be further printable:
            for indexed_element in indexed_elements:
                for element in self.__archive:
                    if element != "Empty" and element.unique_id == indexed_element[1]:
                        indexed_element.append(element.value)

            # Replaces 'free_space' with proper elements:
            try:
                for i in range(self.__archive_size):
                    if i in empty_positions:
                        printable_list[i] = "Empty"
                while True:
                    for indexed_element in indexed_elements:
                        printable_list[printable_list.index("free_space")] = {'ID': indexed_element[1], "value": indexed_element[2], "index_in_archive": indexed_element[0]}
            except ValueError:
                pass

        print(printable_list)
