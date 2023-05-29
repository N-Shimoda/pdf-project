# This program changes the page order of a given PDF files in `input` directory
# After operation, the sorted PDF file forms a BOOKLET when printed.

import pypdf
import glob2

def bind_PDF(src_path, dst_basepath):

    src_pdf = pypdf.PdfReader(src_path, strict=True)  # 'strict=True'?
    secondary_pdf = pypdf.PdfWriter()
    secondary_pdf.append_pages_from_reader(src_pdf)

    # secondary_pdf is made by
    # adding blank pages to the end of given PDF file
    # so that it has "multiple of 4" pages.
    # Precisely speaking, 4*[n/4] pages    ([] is CEILING function)
    n = src_pdf.numPages
    if(n % 4 != 0):
        for i in range(4-n % 4):
            secondary_pdf.addBlankPage()

    dst_pdf = pypdf.PdfFileWriter()
    N = secondary_pdf.getNumPages()
    for i in range(N//4):
        dst_pdf.addPage(secondary_pdf.getPage(-(2*i+1)))
        dst_pdf.addPage(secondary_pdf.getPage(2*i))
        dst_pdf.addPage(secondary_pdf.getPage(2*i+1))
        dst_pdf.addPage(secondary_pdf.getPage(-(2*i+2)))

    with open('{}.pdf'.format(dst_basepath), 'wb') as f:
        dst_pdf.write(f)


if __name__ == "__main__":
    
  files = glob2.glob("./input/*")
  for filename in files:
      # filename = "EXCFG21.pdf"  # Enter the file name HERE.
      bind_PDF(filename, "output/"+filename[8:-4]+"_sorted")