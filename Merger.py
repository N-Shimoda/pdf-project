import sys
# sys.path.append('/opt/anaconda3/lib/python3.8/site-packages')

import PyPDF2
from pathlib import Path

# List of PDF files in the folder
pdf_dir = Path("./pdf_files")
pdf_files = sorted(pdf_dir.glob("*.pdf"))

# Integrate all PDF files into one
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))

# Name of new file is consisted of 
# names of the first and the last files
merged_file = pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

# Save
with open(merged_file, "wb") as f:
    pdf_writer.write(f)