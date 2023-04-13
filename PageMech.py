import Constants
import Processor
import Ram
import random


class PageMech:
    def __init__(self, processor: Processor.Processor, ram: Ram.Ram):
        self.Processor = processor
        self.Ram = ram

    def find_empty_block(self) -> int:
        while self.Ram.BlockInUse[(i := random.randint(0, Constants.user_blocks))]:
            pass
        self.Ram.BlockInUse[i] = True
        return i

    def get_page_mech_block(self) -> None:
        block = self.find_empty_block()
        self.Processor.PTR = block

    def get_blocks(self) -> None:
        self.get_page_mech_block()
        for i in range(Constants.vm_blocks):
            self.get_block(i)

    def get_block(self, i) -> None:
        pass
