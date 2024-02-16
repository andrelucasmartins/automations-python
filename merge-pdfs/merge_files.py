import os

import PyPDF2

merger = PyPDF2.PdfMerger()

list_archives = os.listdir("./archives")
list_archives.sort()

print(list_archives)

for archive in list_archives:
  if ".pdf" in archive:
    merger.append(f"./archives/{archive}")


merger.write("PDF_MERGED.pdf")