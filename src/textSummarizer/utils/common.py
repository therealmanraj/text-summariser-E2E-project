import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any

@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: A ConfigBox object containing the YAML data.
    """

    try:
        with open(path_to_yaml, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    
@typechecked
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories at the specified paths.

    Args:
        path_to_directories (list): A list of paths where directories need to be created.
        verbose (bool, optional): If True, print the created directory paths. Defaults to True.
    """

    for directory_path in path_to_directories:
        directory_path = Path(directory_path)
        os.makedirs(directory_path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {directory_path}")
            
            
@typechecked
def get_size(path: Path) -> str:
    """
    Gets the size of a file or directory in bytes.

    Args:
        path (Path): The path to the file or directory.

    Returns:
        str: The size of the file or directory in bytes.
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"