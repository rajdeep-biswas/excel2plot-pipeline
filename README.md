# Excel2Plot

### Why does this exist?
On one of my earliest work assignments, I was provided with an excel sheet containing various customers and their expenses over multiple months over years, and the usecase was to develop a forecasting feature that uses the "best three" available algorithms on the [SAP HANA PAL](https://help.sap.com/viewer/2cfbc5cf2bc14f028cfbe2a2bba60a50/2.0.03/en-US/c9eeed704f3f4ec39441434db8a874ad.html) library.  
This repository contains the pipeline code that I wrote to assess the performance of all available time-series forecasting algorithms, on said library, in an automated manner.  
On running `Python Helpers/pipeline.py`, each unique commodity is identified from the excel sheet, and an array of the expenses column is generated. If this array is long enough to be performing an analysis on, it is selected for running the prediction algorithms on. `SQL Files/` contains various stored procedures that I wrote for automatic fetching of results.  
The python file also connectes to a HANA Db Runtime via the [HDB CLI](https://pypi.org/project/hdbcli) wrapper for running said stored procedures.  
Once results are obtained, the collated plots are generated and saved as PNG files for visualization. And the CLI shows updated results for each iteration which are derived using a custom rank scoring mechanism that I devised.  
Each iteration of these results are also saved into an external CSV file for future reference.  
  
Also, if the pipeline run gets interrupted due to any reason, I wrote a feature that takes care to just pick up from where it last left off.  

![alt text][Example of a plot]

[Example of a plot]: SavedPlots/Figure_1_New.png "Sample image of what a comparison plot looks like."

### Great, but how do I run the code?

1. Obtain your `svcategory-nocomma.xlsx` or equivalent.  
Relevant columns would be `UNSPSC.AribaCategoryIdL3` (Commodity ID), `AccountingDate.Month1970` (Month Timestamp), `sum(Amount)` (Amount Spent).  
2. Run `excelcolumntolist.py` (this is for preprocessing).
3. Run `pipeline.py`.  

### Project structure (in order of importance).
`Python_Helpers/` is the main directory that contains the driver python code including other helper files.  
`MSE_Log/` contains the CSV that records the scores of each algorithm over each commodity.  
`SQL_Files/` contain stored procedure files with placeholders in them.  
`Saved_Plots/` contain matplotlib exports.  
`PAL_Output_Sheets/` contains excel exports of forecasts of each commodity for manual inspsection.  
`Python_Helpers/Test_Files/` contain older files that were written during development, are not in current use, but still document some progressive (albeit deprecated) functionality.  
`SQL_Files/Prefinal/` contain older developmental test .sql files not currently in use.  