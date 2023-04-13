import os
import Util


class HDD:
    def __init__(self):
        if not os.path.exists(Util.disk_path):
            open(Util.disk_path, 'w').close()
