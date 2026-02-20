import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if os.path.exists(self.filename):
            try:
                os.remove(self.filename)
            except OSError:
                pass

        return None
