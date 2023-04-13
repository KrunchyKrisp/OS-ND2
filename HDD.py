import os
import Constants


class HDD:
    def __init__(self):
        if not os.path.exists(Constants.disk_path):
            open(Constants.disk_path, 'w').close()
