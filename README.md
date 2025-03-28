# EDA-of-flightprice-dataset
Flight Price Data Preprocessing & Feature Engineering
The dataset used is Data_Train.xlsx, which contains details about various flight journeys including airlines, source/destination cities, departure/arrival times, total stops, duration, and other metadata.
To preprocess and transform raw flight data into a structured format suitable for machine learning models. The focus is on:

Handling date/time features

Dealing with missing values

Encoding categorical variables

Dropping irrelevant or redundant columns

Converting object types to numeric for model compatibility

Steps Performed
1. Date Feature Extraction
The Date_of_Journey column is split into Day, Month, and Year.

These columns are converted from string to integer types.

The original Date_of_Journey column is dropped.

2. Arrival Time Processing
The Arrival_Time column includes both time and sometimes a date. Only the time is extracted.

Time is split into Arrival_Hour and Arrival_Min, both converted to integers.

The original Arrival_Time column is dropped.

3. Departure Time Processing
The Dep_Time is split into Dep_hour and Dep_min, and converted to integers.

The original Dep_Time column is dropped.

4. Duration Feature Engineering
The Duration column is split into Duration_hour and Duration_min using regular expressions.

Missing durations are filled with zeros and converted to integers.

The original Duration column is dropped.

5. Dropping Redundant Columns
Columns like Route and Additional_Info (after encoding) are dropped as they either duplicate other information or add little value.

6. Handling Nulls and Duplicates
Checked for null values and duplicates to ensure data integrity.

7. Encoding Categorical Variables
Used OneHotEncoder from sklearn to one-hot encode columns: Airline, Source, Destination, and Additional_Info.

The resulting encoded columns are concatenated back to the main DataFrame.

Original categorical columns are then dropped.

8. Mapping Stop Information
Total_Stops is a categorical feature (e.g., "non-stop", "1 stop", etc.) and is mapped to numerical values (e.g., 0, 1, 2, etc.).

Final Output
A fully preprocessed and numeric dataset (data_nw) ready for training machine learning models like regression, decision trees, XGBoost, etc.

Tools & Libraries Used
Python
pandas
numpy
scikit-learn
