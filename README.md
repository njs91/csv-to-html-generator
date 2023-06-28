# CSV to HTML Converter

This Python script (`csv_to_html.py`) converts data from a CSV file into
HTML content. It generates an HTML representation of each row in the CSV
file, following a specific format.

## Usage

Follow the steps below to use the `csv_to_html.py` program:

1. **Download the code**: Download the `csv_to_html.py` file from the
   repository or copy the code into a new file named `csv_to_html.py`.

2. **Rename CSV**: Rename `pulse-rows-generator-content-default.csv` to `pulse-rows-generator-content.csv` and use THAT file (since it'll be inside gitignore).

3. **Prepare the CSV file**: Make sure you have the
   `pulse-rows-generator-content.csv` file ready. If needed, create or modify
   the CSV file with the desired content. Ensure that the CSV file has a
   header row with the following column names: "Source", "Description",
   "Filename", and "Extension".

4. **Move the files to the same directory**: Place the `csv_to_html.py`
   and `pulse-rows-generator-content.csv` files in the same directory or
   folder.

5. **Run the program**: Open a terminal or command prompt, navigate to the
   directory where the `csv_to_html.py` file and the CSV file are located.

6. **Execute the script**: Run the script by executing the following
   command:

   ```bash
   python csv_to_html.py
   ```

7. **View output**: The HTML will be in a file called output.html (gitignored)

8. **Insert in the right place**: It might need to be placed in this (crappy) HTML structure:

   ```
   <div class='demo_page_subtitle_wrap'>
        <demo_page_subtitle>
            <p id="2023"><a href="#2023">2023</a></p>
        </demo_page_subtitle>
        <article class='file-table'>
          <div class='row'>
            <span>Source</span>
            <span>Description</span>
            <span>Filename</span>
          </div>
          rows...
        </article>
      </div>
   ```
