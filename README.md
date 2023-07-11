# Task: Construct visualizations for each assigned table.

Your assigned tables can be found in the pinned messages of the main telegram group.

Copy the `appends_clean.ipynb` then rename it to `your_name.ipynb`

- In the content of the copied and renamed file, complete your tasks after the last line of the code in the original file.
- Each codebox of your copied and renamed file must contain a comment `#your_name` on the top before the start of any code.
  - For example
    <hr>
    
    ```python
    # Pitou
    ...
    df = pd.read_csv('Data/Data_of_Attack_Back.csv')
    ...
    ```

    <hr>
- Your variables naming convention must start with the name of the table you are working on.
  - For example
    <hr>

    ```python
    # Pitou
    ...
    # Data_of_Attack_Back -- Setting the x axic as EXAMPLE and y axis
    ...
    Data_of_Attack_Back_fig, Data_of_Attack_Back_ax = plt.subplots(nrows=1, ncols=1, figsize=(120,40))
    ...
      
    ```

    <hr>
