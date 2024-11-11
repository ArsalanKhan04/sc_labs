import os
import pytest
import tempfile
from FileSearch import filesearch as recursive_search

# Test 1: File exists at the top level
def test_file_in_top_level():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "target_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")
        
        cnt = recursive_search(temp_dir, ["target_file.txt"])
        assert (cnt > 0)

# Test 2: File exists in a nested subdirectory
def test_file_in_nested_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        nested_dir = os.path.join(temp_dir, "subdir")
        os.mkdir(nested_dir)
        file_path = os.path.join(nested_dir, "target_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")
        
        cnt = recursive_search(temp_dir, ["target_file.txt"])
        assert (cnt > 0)

# Test 3: File does not exist
def test_file_not_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.mkdir(os.path.join(temp_dir, "subdir"))
        cnt = recursive_search(temp_dir, ["missing_file.txt"])
        assert (cnt == 0)

# Test 4: Multiple files with the same name
def test_multiple_files_with_same_name():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path1 = os.path.join(temp_dir, "target_file.txt")
        nested_dir = os.path.join(temp_dir, "subdir")
        os.mkdir(nested_dir)
        file_path2 = os.path.join(nested_dir, "target_file.txt")

        with open(file_path1, "w") as f:
            f.write("Top-level file content")
        with open(file_path2, "w") as f:
            f.write("Nested file content")
        cnt = recursive_search(temp_dir, ["target_file.txt"])
        assert (cnt > 1)


# Test 5: Empty directory
def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert recursive_search(temp_dir, "target_file.txt") == 0

# Test Case Sensitivity
def test_case_sensitivity():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "target_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")
        
        cnt = recursive_search(temp_dir, ["TARGET_FILE.TXT"], casesensitive=True)
        assert (cnt == 0)

# Test Case Insensitivity
def test_case_insensitivity():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "target_file.txt")
        with open(file_path, "w") as f:
            f.write("Test content")
        
        cnt = recursive_search(temp_dir, ["TARGET_FILE.TXT"], casesensitive=False)
        assert (cnt > 0)

