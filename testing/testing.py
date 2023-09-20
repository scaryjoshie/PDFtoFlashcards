# imports
import pdfkit

# Turns pdf file into an html file
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

html_file = pdfkit.from_file(input="textbook.pdf", output_path="output")

#
with open("output\\output.html", "w") as f:
    f.write(html_file)