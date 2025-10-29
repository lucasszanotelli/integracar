from docling.document_converter import DocumentConverter
from pathlib import Path

# conv = DocumentConverter()   # usa defaults
pdf = Path("docs/Decreto Estadual n° 3.346-R, de 11 de julho de 2013.pdf")

result = DocumentConverter().convert(pdf).document

export = getattr(result, "export_to_text", None)
# Exporte para Markdown e JSON:
# md = result.export_to_markdown()
# js = result.export_to_html()
text = result.export_to_text()


# open("saida.md", "w", encoding="utf-8").write(md)
# open("saida.html", "w", encoding="utf-8").write(js)
open("saida.txt", "a", encoding="utf8").write(text)
