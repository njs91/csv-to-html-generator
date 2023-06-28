import csv


def generate_html_from_csv(csv_file):
    html_content = ""
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            source = row["Source"]
            description = row["Description"]
            filename = row["Filename"]
            extension = row["Extension"]

            html_content += """
                <div class='row gen'>
                  <span class='source'>{}</span>
                  <span class='description'>{}</span>
                  <span class='file'><a href='{}' target='new'>{}</a></span>
                </div>
            """.format(
                source,
                description,
                filename + "." + extension,
                filename + "." + extension,
            )

    return html_content


csv_file_path = "pulse-rows-generator-content.csv"
html = generate_html_from_csv(csv_file_path)

output_file = "output.html"
with open(output_file, "w") as file:
    file.write(html)

print("HTML content has been saved to {}.".format(output_file))
