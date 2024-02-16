# Merge pdfs

add your pdf's on the [archives]() directory and rename follow example:

```block
01-myFile.pdf
02-myFile.pdf
```

This generates an array with this:

```bash
['01-myFile.pdf', '02-myFile.pdf']
```

Now run the program using this command:
```bash
C:/Python310/python.exe d:/Project/automations-python/merge-pdfs/merge_files.py
```
End finally, now was generate new PDF merge and you can verify on the root.

<pre>
|--merge-pdfs
|---archives
    |--01-myFile.pdf
    |--02-myFile.pdf
|---PDF_MERGED.pdf
|---README.md
</pre>
