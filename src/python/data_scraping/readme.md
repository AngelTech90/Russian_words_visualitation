# Introduction
The script uses *pandas* and *pathlib* module for data extraction from a main .csv file that contains all words to separate .txt files 

We make it simple, the takes one column and take all tuples in a single .txt file 

## Dependencies installation:
```bash
pip install pandas
```

## Code structure of script 

We have a function named *extract_first_column* that receive *csv file path* and *output_file* it's a predefined parameter


#### We abstract our csv file as a code element:
```python
df = pd.read_csv(csv_file_path)
```

#### We use *.iloc* built-in method of pandas for get one of the able columns and rows of that column on our .csv file 

```python
column = df-iloc[:,0]
```

**In this example we first get all rows of first column in our file, using 0 as reference like an array**

### Then, we just create a file that will use a for loop to get all elements from column and write it in a txt file

```python
with open(output_file,`w`, encoding='utf-8') as f:
  for value in column:
    if pd.notna(value):
      f.write('f{value}\n')
```
**Only thing special on this code is that we'll skip void values in .csv file**


