# Prefix-to-postfix_recursive

[![Viewers](https://hits.sh/github.com/vtangstastic/prefix-to-postfix_recursive.svg)](https://hits.sh/github.com/vtangstastic/prefix-to-postfix_recursive/)


**Description:**
This project converts prefix expressions to postfix expressions. It includes a Python script that performs the conversion and provides a help menu for usage.

---

**Usage:**
To run the help menu, use the following command:
```
python -m proj2 -h
```

To execute the conversion with the provided input and output files, use the following commands:
```
python -m proj2 resources/in.txt resources/out.txt
```

---

**Input Files:**
- `resources/in.txt`: Contains prefix expressions to be converted.
- `resources/extra_in.txt`: Additional input files can be added here.

---

**Output Files:**
- `resources/out.txt`: Contains the corresponding postfix expressions.
- `resources/extra_out.txt`: Additional output files will be generated here.

---

**Files:**
1. **main.py:** Contains the main script for executing the conversion.
2. **prefix_to_postfix.py:** Contains the class responsible for converting prefix expressions to postfix.
3. **in.txt:** Sample input file with prefix expressions.
4. **out.txt:** Corresponding output file with postfix expressions.

---

**How to Run:**
1. Ensure Python is installed on your system.
2. Navigate to the project directory.
3. Run the script with the provided input and output files using the command:
```
python -m proj2 resources/in.txt resources/out.txt
```

---

**Note:**
Ensure that the input file paths are correctly specified, and the output directories have appropriate write permissions. If additional input files are required, place them in the `resources` directory and follow the same naming convention.
