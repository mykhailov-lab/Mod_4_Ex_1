def load_initial (filename: str) -> list[str]:
    try:
        with open (filename, 'r', encoding='utf-8') as file :
            return file.readlines()
    except FileNotFoundError:
        return []

