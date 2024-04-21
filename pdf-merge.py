#!/usr/bin/python3
import os
import argparse
from tqdm import tqdm
from pypdf import PdfWriter

def merge_pdfs(directory, output_file="merged-pdf.pdf"):
    contents = sorted(os.listdir(directory))

    # Filter out directories and non-PDF files
    pdfs = [file for file in contents if file.endswith(".pdf")]

    merger = PdfWriter()

    with tqdm(total=len(pdfs)) as progress:
        for pdf in pdfs:
            pdf_path = os.path.join(directory, pdf)
            progress.set_description(pdf)
            merger.append(pdf_path)
            progress.update(1)

    output_path = os.path.join(directory, output_file)
    merger.write(output_path)
    merger.close()
    print("Merged " + str(len(pdfs)) + " pdf files to: " + output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge PDFs in a directory")
    parser.add_argument("-d", "--directory", default=".", help="Directory containing PDFs to merge")
    parser.add_argument("-o", "--output", default="merged-pdf.pdf", help="Output filename for merged PDF (default: merged-pdf.pdf)")
    args = parser.parse_args()

    merge_pdfs(args.directory, args.output)
