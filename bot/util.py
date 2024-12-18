import os


def get_root_directory():
    current_file = __file__
    root_dir = os.path.dirname(os.path.abspath(current_file))
    return root_dir


def get_path(product_name):
    root_dir = get_root_directory()
    assets_path = os.path.join(root_dir, "bot", "assets")
    path = os.path.join(assets_path, product_name)
    return path

