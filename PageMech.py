import Util
import Processor
import Ram
import random


class PageMech:
    def __init__(self, processor: Processor.Processor, ram: Ram.Ram):
        self.Processor = processor
        self.Ram = ram

    def find_empty_block(self) -> int:
        i = 0

        # try 16 times for a random block
        for _ in range(16):
            i = random.randint(0, Util.user_blocks)
            if not self.Ram.BlockInUse[i]:
                break

        # find first empty block if not found
        if self.Ram.BlockInUse[i]:
            try:
                i = self.Ram.BlockInUse.index(False)
            except ValueError:
                raise Exception('Ram is full')

        self.Ram.BlockInUse[i] = True
        return i

    def get_page_mech_block(self) -> None:
        block = self.find_empty_block()
        self.Processor.PTR = block

    def get_blocks(self) -> None:
        self.get_page_mech_block()
        for i in range(Util.vm_blocks):
            self.get_block(i)

    def get_block(self, i) -> None:
        self.Ram.set_word(self.Processor.PTR, i, self.find_empty_block())

