# Data Engineering Pipeline Project

## Project Overview
This project demonstrates a complete **data engineering workflow** including:
- Data cleaning and preprocessing
- Exploratory data analysis
- SQL-based querying
- Generating insights for decision-making  

The project is implemented using Python (Jupyter Notebook) and SQL queries.  

---

## Folder Structure
The project is organized as follows:

MyDataProject/
├─ notebooks/ # Jupyter notebooks with code and analysis
│ └─ my_analysis.ipynb
├─ src/ # Python scripts if any
│ └─ (optional .py files)
├─ sql/ # SQL queries
│ └─ query1.sql
│ └─ query2.sql
├─ README.md # This file
├─ requirements.txt # List of Python packages (optional)


---

## Approach (Step by Step)

1. **Data Loading**
   - Load the raw dataset using Pandas/Spark.
   - Inspect the dataset for general structure, missing values, and data types.

2. **Data Cleaning**
   - **Missing values:** Filled or imputed based on median/mean or dropped if necessary.
   - **Duplicates:** Removed rows with identical identifiers.
   - **Outliers:** Handled by capping values beyond the 99th percentile.
   - **Date/Time formatting:** Converted date strings to datetime objects.
   - **Type conversions:** Ensured correct data types for analysis and SQL queries.

3. **Data Transformation**
   - Created new features/columns as required for analysis.
   - Aggregated data for reporting (e.g., monthly sales, customer segments).

4. **Analysis and SQL Queries**
   - Queries written to extract insights such as top customers, average order values, and product trends.
   - Example queries are stored in the `sql/` folder.

5. **Visualization (Optional)**
   - Graphs and charts generated to summarize key findings.

---

## Assumptions Made While Cleaning
- Missing values in numeric columns were filled with the **median**.
- Missing categorical values were filled with the **mode** or marked as `"Unknown"`.
- Duplicate entries were removed based on a **unique ID column**.
- Outliers were capped at the **99th percentile** to reduce skewness.
- Date columns were assumed to follow a consistent format for parsing.

---

## How to Run the Code

1. **Clone the repository**

```bash
git clone https://github.com/Sharath9281/Data-Engineering-Pipeline.git
cd \path\to\the\projrct
```
2. **Create and Activate a Python Virtual Environment**
```bash
python -m venv env
# On Windows
env\Scripts\activate
# On Mac/Linux
source env/bin/activate
```
3.**Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the notebook**
```bash
jupyter notebook notebooks/Data Engineering Pipeleine.ipynb
```
##Note 
 *You need to create the tables in the postgresql to store the data 
