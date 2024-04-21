
# Project Title

I got tired and sick of using online PDF mergers and covertors who kept pushing me into signing up for a subcription or took too long to stick some PDFs together, and I'm still not crazy enough to do so using Word or LibreOffice Writer, so I made my own in python.
![nerd](https://github.com/n-amsomn/Python-Utilities-Tool/blob/master/image.gif?raw=true)
## Installation

Just clone into the project using git clone.

If you wish to make it executable from anywhere you might wanna add it to your $PATH (I added mine as 'pdfmrg'), don't forget to:

```bash
    chmod +x pdf-merge.py
```
    
## Documentation

You can pass two flags to the script:

```
    pdfmerge -f path/to/the/directory -o output_file.pdf
```

By default it uses the current working directory and the default file name is "merged-pdf.pdf"
## Usage/Examples
If you don't have an alias assigned to the command you'll have to specify the full path or just copy the PDFs inside the script folder and run the script.

An example to merge all PDFs inside your Documents folder and name it "giant_blob_of_files.pdf"
```python
    python3 pdf-merge.py -f ~/Documents/ -o giant_blob_of_files.pdf
```
Or if you prefer just throw them in the same folder and just run it simple with:

```python
    python3 pdf-merge.py
```
