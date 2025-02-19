# Optima Task

This project processes race results and outputs them to JSON files. The main script is written in Python and uses `pandas` to handle data processing. The results are filtered by positions and years and output to JSON files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Description](#code-description)
- [Consideratons for cloud deployment](#Consideratons-for-cloud-deployment)

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
1. Positions: Default value is 1 to satisfy requirements. This can however be ran to return results for any position/ mix (Although in the current setup it doesn't output position to stick to requirements)
2. Years: Default value is None, this means it will run for all available years. However, the user can specify a year or years to run for.

```sh
python main.py --positions 1 2 3 --years 2021 2022
```

## Code Description

The script processes race results by:

1. Loading race and result data from CSV files.
2. Preparing the race and result data.
3. Combining the race and result data.
4. Sorting and filtering the data.
5. Outputting the yearly results to JSON.

## Consideratons for cloud deployment

1. Data storage & ingestion: The CSV inputs will need to be ingested into a cloud provider such as AWS or Azure.
2. Data processing playform: Once the data is stored in the cloud, it needs to be interacted with. A platform such as databricks is ideal for this. The repo can then be cloned into a gitfolder in databricks.
3. Workflows & Triggers: Set up a workflow & define the required cluster, decide on a trigger/ notification setup that will run the workflow.
4. Data accerss: How does the user wanrt to access the resulting JSON files?
5. Scalability: Spark dataframes can work with large datasets more effectively, consider switching to this in a cloud enviroment.
6. Cost management: Monitor and optimise reasource usage.
7. Unit testing: Implement unit testing to test specific methods in isolation.
8. Security: Ensure correct access levels.

