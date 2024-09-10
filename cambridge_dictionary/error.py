class NotFoundWord(Exception):
    def __init__(self, word):
        super().__init__(f"Từ {word} không tồn tại")

class ApiError(Exception):
    def __init__(self, *args):
        super().__init__("Đã xảy ra sự cố với api", *args)