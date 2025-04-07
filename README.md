# Nobel Prize Winners!

Statistics of Nobel Prize Laureates.

This repository provides a simple analysis of Nobel Prize winners using Python and pandas. The script displays information about recent Nobel laureates and analyzes the distribution of prizes by category.

## Dataset

The dataset includes the following columns:

- **Year**: The year the prize was awarded.
- **Category**: The category of the Nobel Prize (e.g., Peace, Literature).
- **Laureate**: The name of the individual or organization that won.

### Example Data:

| Year | Category     | Laureate                 |
|-----|--------------|---------------------------|
| 2020 | Peace        | World Food Programme       |
| 2019 | Literature   | Peter Handke               |
| 2018 | Physics      | Donna Strickland            |
| 2017 | Chemistry    | Frances Arnold              |
| 2016 | Medicine     | Yoshinori Ohsumi            |

## Python Script

The script `nobel_prize_winners.py` performs the following tasks:

- Loads a small dataset of recent Nobel Prize winners.
- Displays the data in a tabular format.
- Analyzes the number of winners by category.
- Saves the data to a CSV file (`nobel_prize_winners.csv`).

## Requirements

- Python 3.x
- pandas library

To install the pandas library, use:
```bash
pip install pandas
