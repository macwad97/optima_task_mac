import os
import pandas as pd
import json

def main(positions=[1], years=None):
    """
    Main function to process race results and output to JSON files.

    Parameters:
    positions (list): List of finishing positions to filter the results. Default is [1]. (You can enter multiple positions, however it will not specify in the JSON as I wanted to stick to the requirments)
    years (list): List of years to filter the races. Default is None, which includes all years.
    """
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Import races & results
    races, results = load_data(script_dir)
    
    # Data prep
    races = races_prep(races, years)
    results = results_prep(results, positions)
    
    # Combine race result and race details
    race_results = pd.merge(races, results, on='raceId')
    
    # Sort the results by year & round
    race_results.sort_values(by=['year', 'round'], inplace=True)
    
    # Find years in data
    years = race_results['year'].unique()
    
    # Loop through each year and output to JSON
    for year in years:
        output_json(race_results, year, script_dir)

def load_data(script_dir):
    """
    Load races and results data from CSV files.

    Parameters:
    script_dir (str): The directory of the script.

    Returns:
    tuple: Two Pandas DataFrames, one for races and one for results.
    """
    # Construct the paths to the CSV files relative to the script folder
    races_file = os.path.join(script_dir, '..', 'source-data', 'races.csv')
    results_file = os.path.join(script_dir, '..', 'source-data', 'results.csv')
    
    # Load the CSV data into Pandas DataFrames
    races = pd.read_csv(races_file)
    results = pd.read_csv(results_file)
    
    return races, results

def races_prep(df, years):
    """
    Prepare the races DataFrame by filtering by years (when required) and creating datetime columns.

    Parameters:
    df (DataFrame): The races DataFrame.
    years (list): List of years to filter the races. Default is None, which includes all years.

    Returns:
    DataFrame: The prepared races DataFrame.
    """
    # When specified, limit to entered years
    if years is not None:
        df = df[df['year'].isin(years)]

    # Use default time where missing
    df['time'] = df['time'].fillna('00:00:00')
    
    # Create datetime column
    df['datetime_string'] = df['date'] + 'T' + df['time']
    
    return df

def results_prep(df, positions):
    """
    Prepare the results DataFrame by filtering by positions and filling fastest lap times when not available.

    Parameters:
    df (DataFrame): The results DataFrame.
    positions (list): List of finishing positions to filter the results.

    Returns:
    DataFrame: The prepared results DataFrame.
    """
    # Limit results df to finishing positions of interest (Removes unnecessary data)
    df = df[df['position'].isin(positions)]
    
    # Set fastest lap time to zero when missing
    df['fastestLapTime'] = df['fastestLapTime'].fillna('00:00.0')
    
    return df

def output_json(df, year, script_dir):
    """
    Output the race results for a specific year to a JSON file.

    Parameters:
    df (DataFrame): The combined race results and race details DataFrame.
    year (int): The year to filter the races.
    script_dir (str): The directory of the script.
    """
    # Limit to races for current year
    df_year = df[df['year'] == year]
    
    # Define output filepath
    filepath = os.path.join(script_dir, '..', 'results', f'stats_{year}.json')
    
    # Create a dictionary with the desired structure
    json_list = df_year.apply(
        lambda row: {
            "Race Name": row["name"],
            "Race Round": row["round"],
            "Race Datetime": row["datetime_string"],
            "Race Winning driverId": row["driverId"],
            "Race Fastest Lap": row["fastestLapTime"]
        }, axis=1).tolist()
    
    # Convert the list to a JSON string and save to a file
    with open(filepath, 'w') as json_file:
        json.dump(json_list, json_file, indent=4)
    
    print(f"Output saved to {filepath}")

if __name__ == '__main__':
    main()
