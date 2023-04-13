import Constants


class Ram:
    def __init__(self):
        self.Memory = [0 for _ in range(Constants.total_bytes)]
        self.BlockInUse = [False for _ in range(Constants.ram_blocks)]

    def set_byte(self, block, word, byte, value):
        self.Memory[
            block * Constants.block_length * Constants.word_length
            + word * Constants.word_length
            + byte] = value

    def set_word(self, block, word, value):
        pass
