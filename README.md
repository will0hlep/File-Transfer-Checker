Script for checking that all files in the origin folder have been successfully copied to the destination folder. Uses `os.walk` to build a list of all file paths in the origin_path directory and any subdirectories. Then for each file path the script checks that the same file path exists within the destination directory. To run open the command prompt to the same folder as this script is saved and use the following command:

```
python3 transfer_check.py <ORIGIN_PATH> <DESTINATION_PATH>
```

If origin or destination paths have spaces, enclose them in quotation marks in the command.