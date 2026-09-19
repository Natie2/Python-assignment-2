"""Question 5: An abstract FileHandler with concrete Text and Binary subclasses."""

from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Contract that every file handler must honour."""

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        """Return the contents of the file."""

    @abstractmethod
    def write(self, data):
        """Write data to the file."""

    # A concrete method - shared by every subclass, no need to re-implement
    def describe(self):
        return f"{self.__class__.__name__} managing '{self.filename}'"


class TextFileHandler(FileHandler):
    """Reads and writes UTF-8 text."""

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

    def write(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(data)


class BinaryFileHandler(FileHandler):
    """Reads and writes raw bytes."""

    def read(self):
        with open(self.filename, "rb") as file:
            return file.read()

    def write(self, data):
        with open(self.filename, "wb") as file:
            file.write(data)


if __name__ == "__main__":
    text_handler = TextFileHandler("notes.txt")
    text_handler.write("Encapsulation, inheritance, polymorphism, abstraction.")
    print(text_handler.describe())
    print("Read back:", text_handler.read())

    binary_handler = BinaryFileHandler("data.bin")
    binary_handler.write(b"\x50\x59\x54\x48\x4f\x4e")
    print(binary_handler.describe())
    print("Read back:", binary_handler.read())

    # Polymorphism: the loop does not care which subclass it is holding
    print("\nPolymorphic loop:")
    for handler in (text_handler, binary_handler):
        print(" ", handler.describe(), "->", len(handler.read()), "units read")

    # Proof that the abstract class cannot be instantiated
    print("\nTrying to instantiate FileHandler directly:")
    try:
        FileHandler("anything.txt")
    except TypeError as error:
        print("  Blocked ->", error)
