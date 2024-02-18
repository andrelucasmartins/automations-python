import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="Select Folder")

list_files = os.listdir(path)

local = {
  "images": [".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".avif", ".jfif"],
  "videos": [".avi", ".mp4", ".mov", ".mkv", ".m4a"],
  "audios": [".mp3", ".wav", ".ogg", ".aac", ".flac", ".ape", ".wma", ".opus", ".webm"],
  "pdfs": [".pdf", ".PDF"],
  "excel": [".xlsx", ".xls"],
  "csv": [".csv"],
  "zip": [".zip", ".rar", ".7z"],
  "docs": [".docx", ".doc", ".txt"],
  "json": [".json"],
  "html": [".html", ".htm"],
  "xml": [".xml"],
  "java": [".java", ".java"],
  "sql": [".sql"],
  "exe": [".exe"],
  "powerpoint": [".pptx", ".ppt", ".odp"],
}

for file in list_files:
  name, extension = os.path.splitext(f"{path}/{file}")
  for folder in local:
    if extension.lower() in local[folder]:
      if not os.path.exists(f"{path}/{folder}"):
        os.mkdir(f"{path}/{folder}")
      os.rename(f"{path}/{file}", f"{path}/{folder}/{file}") 
      
    