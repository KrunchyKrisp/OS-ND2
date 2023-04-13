import struct

import Util


class Ram:
    def __init__(self):
        self.Memory = [b'0' for _ in range(Util.total_bytes)]
        self.BlockInUse = [False for _ in range(Util.ram_blocks)]

    def set_byte(self, block: int, word: int, byte: int, value: bytes) -> None:
        self.Memory[
            block * Util.block_length * Util.word_length
            + word * Util.word_length
            + byte] = value

    def set_bytes(self, block: int, word: int, value: [bytes]) -> None:
        for i, b in enumerate(value):
            self.set_byte(block, word, i, b)

    def set_word(self, block: int, word: int, value: int) -> None:
        self.set_bytes(block, word, Util.int_to_hex(value))

    def get_byte(self, block: int, word: int, byte: int) -> bytes:
        return self.Memory[
            block * Util.block_length * Util.word_length
            + word * Util.word_length
            + byte]

    def get_bytes(self, block: int, word: int) -> [bytes]:
        i = block * Util.block_length * Util.word_length + word * Util.word_length
        return self.Memory[i:i + 4]

    def get_word(self, block: int, word: int) -> int:
        return Util.hex_to_int(self.get_bytes(block, word))
