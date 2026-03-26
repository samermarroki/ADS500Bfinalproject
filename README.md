# Bank Marketing Data Preprocessing

## Data Import

The dataset used in this project is the Bank Marketing dataset, stored as a CSV file. Because the file is semicolon-delimited rather than comma-delimited, it is imported in Python using `pandas.read_csv()` with `sep=';'`. After loading the file, the dataset is inspected to confirm its dimensions, column names, data types, and the presence of missing values. This initial profiling step helps verify that the data has been read correctly and provides a clear overview of the structure of the dataset before any preprocessing is performed.

The imported dataset contains 45,211 rows and 17 columns. The variables include a mix of numeric and categorical features, such as customer age, balance, contact type, campaign information, and the target variable `deposit`. During the import review, both standard missing values and placeholder values such as `unknown` are identified, since these require special handling during preprocessing.

## Data Preprocessing

The preprocessing stage begins by standardizing the dataset structure. Column names are cleaned by converting them to lowercase and replacing spaces with underscores to make them easier to reference in code. Categorical text values are stripped of extra spaces and converted to lowercase to ensure consistency. Duplicate rows are checked and removed if found.

Missing data is then handled using a combination of imputation and category replacement. For the numeric variable `age`, missing values are filled using the median age within each job category, followed by the overall median where needed. For categorical variables such as `job`, `education`, and `default`, missing values are replaced with the most frequent category. Placeholder values such as `unknown` are treated as missing in selected columns, while indicator flags are created to preserve the information that those values were originally unknown.

After cleaning, several transformation techniques are applied to improve the usefulness of the dataset. New features are constructed, including indicators for whether a client was previously contacted, whether the client has any loan, and ratios such as balance per contact and duration per contact. The `month` variable is converted into a numerical month index and grouped into calendar quarters. Need-based discretization is also performed by grouping `age`, `balance`, and `campaign` values into meaningful bands. In addition, min-max normalization is applied to selected numeric variables so they can be compared on a common scale.

Finally, redundant information is reduced by removing columns that have been replaced by more informative derived features. For example, the original textual `month` column is removed after creating `month_num`, and the original `pdays` variable is removed after deriving a cleaner previous-contact feature. The cleaned, transformed, and reduced datasets are then saved as separate output files for further analysis or modeling.

## Project Files

- `bank_marketing_preprocessing.py`: end-to-end preprocessing script
- `bank_marketing_preprocessing_notebook.ipynb`: notebook version of the workflow
- `bank_marketing_outputs/`: generated cleaned, transformed, reduced, and aggregated CSV files
