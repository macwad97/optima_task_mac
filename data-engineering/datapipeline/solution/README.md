# Optima Task

This project processes race results and outputs them to JSON files. The main script is written in Python and uses `pandas` to handle data processing. The results are filtered by positions and years and output to JSON files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Description](#code-description)

## Installation

To run this script, you will need Python installed on your machine along with the necessary Python libraries. Here's how you can set it up:

```sh
# Clone the repository
git clone https://github.com/macwad97/optima_task_mac.git

# Install the required libraries
pip install pandas
```

## Usage
You can run the script with the default parameters or specify the finishing positions and years to filter the results.

### Running the script
To run the script with the default parameters:

```sh
python main.py
```

To run the script with specific positions and years:

```sh
python main.py --positions 1 2 3 --years 2021 2022
```

## Code Description

The script processes race results by:

1. Loading race and result data from CSV files.
2. Preparing the race and result data.
3. Combining the race and result data.
4. Sorting and filtering the data.
5. Outputting the results to JSON.

