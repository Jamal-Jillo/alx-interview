# log parsing

The script first defines a dictionary called status_codes to keep track of the number of lines by status code. It initializes the dictionary with keys for each possible status code and sets their values to zero.

It then initializes the total_size variable to zero and a counter variable to keep track of the number of lines read.

The script then enters a try block that reads input from stdin line by line. For each line, it tries to parse the line and extract the status code and file size. If the line doesn't match the expected format, the script skips the line and moves on to the next one.

If the line matches the expected format, the script updates the metrics by adding the file size to the total_size variable and incrementing the count of the corresponding status code in the status_codes dictionary. It also increments the counter variable.

After every 10 lines, the script prints the current metrics by printing the total file size and the number of lines by status code, sorted in ascending order.

If the script is interrupted by a keyboard interruption (CTRL + C), it handles the interruption by printing the final metrics. It prints the total file size and the number of lines by status code, sorted in ascending order.