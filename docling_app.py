# pip install docling transformers
# (opcional) para usar só o core com tokenizers HF:
# pip install 'docling-core[chunking]'
from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker  # token-aware sobre chunking hierárquico

# tokenizer compatível com seu modelo de embedding (HF)
from transformers import AutoTokenizer
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer

EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = HuggingFaceTokenizer(tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID, max_tokens = 500),
                                 # opcional: limite de tokens por chunk
                                 # max_tokens=512
                                 )

# 1) Converter para DoclingDocument
pdf = Path("docs/Decreto Estadual n° 3.346-R, de 11 de julho de 2013.pdf")
doc = DocumentConverter().convert(pdf).document

# 2) Criar chunker (mescla/splita pensando em tokens)
chunker = HybridChunker(tokenizer=tokenizer, merge_peers=True)
chunks_iter = chunker.chunk(dl_doc=doc)

# 3) Usar os chunks
chunks = []
for ch in chunks_iter:
    # contextualize() injeta cabeçalhos/legendas úteis para embedding
    text_for_embed = chunker.contextualize(ch)
    meta = ch.meta  # tem refs de página, tipo (tabela, parágrafo), cabeçalhos etc.
    chunks.append({"text": text_for_embed, "meta": meta})
    

#### salvar os chunks em markdown
with open("saida_chunks.md", "w", encoding="utf-8") as f:
    for i, ch in enumerate(chunks):
        f.write(f"## Chunk {i+1}\n\n")
        f.write(ch["text"] + "\n\n")