class EmptyPositionArray:

    def __init__(self, size_of_archive: int) -> None:
        self.__array = [x for x in range(size_of_archive)]
        self.__first_empty_position = self.__array[0]

    def add_empty_position(self, empty_position_index: int) -> None:
        """
        Function add_empty_position

        Appends a new empty position to empty_positions array.
        Makes sure that the first empty position is always located at index [0].

        Args:
            empty_position_index (int): element's index in archive structure.

        Return:
            None
        """

        self.__array.append(empty_position_index)
        self.__array = sorted(self.__array) # Verify relevance of adding this later!
        """ 
            Possible way to avoid using sorted method is by checking if 
            empty_position_index < first_array_element, in order to change places:
            -> insert(empty_position_index, 0)

            Certainly not the best performance options.
        """
        self.first_empty_position = self.__array[0] 

    def use_empty_position(self) -> int:
        """
        Function use_empty_position

        Pop used empty position from array and returns it for further manipulations.

        Raises:
            ValueError: if there ain't empty positions

        Returns:
            int: "index" of used empty position
        """
        if len(self.__array) != 0:
            return self.__array.pop(0)
        else:
            raise ValueError("There's no empty positions available.")

    @property
    def array(self) -> list:
        return self.__array

    @property
    def first_empty_position(self) -> int:
        return self.__first_empty_position
    
    @first_empty_position.setter
    def first_empty_position(self, first_empty_position) -> None:
        if isinstance(first_empty_position, int):
            self.__first_empty_position = first_empty_position
