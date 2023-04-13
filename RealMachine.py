import Constants
import Processor
import Ram
import HDD
import PageMech


class RealMachine:
    def __init__(self):
        self.Processor = Processor.Processor()
        self.Ram = Ram.Ram()
        self.HDD = HDD.HDD()
        self.PageMech = PageMech.PageMech(self.Processor, self.Ram)
        self.show_steps = False

    def run(self) -> None:
        while True:
            commands = input().split(' ')

            if commands[0] == 'exec' and len(commands) == 2:
                self.exec_program(commands[1])
            elif commands[0] == 'show':
                self.show_steps = not self.show_steps
                print(f'{self.show_steps = }')
            elif commands[0] == 'quit':
                break
            else:
                print(f'Unrecognized input {commands}')

    def exec_program(self, name):
        found_head = False
        found_program = False
        with open(Constants.disk_path, 'r') as f:
            for line in f:
                if not found_head and line.strip() == 'HEAD':
                    found_head = True
                elif found_head and line.strip() == name:
                    found_program = True
                elif found_program and line.strip() != 'FOOT':
                    pass    # PARSE PROGRAM
                elif found_program and line.strip() == 'FOOT':
                    break
                else:
                    found_head = False
                    found_program = False
