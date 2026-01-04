from domovai.models.code_chunk import CodeChunk
from domovai.models.source_file import SourceFile

def chunk_source(source: SourceFile, lines_per_chunk: int = 50) -> list[CodeChunk]:
    lines = source.content.splitlines()
    chunks: list[CodeChunk] = []

    for i in range(0, len(lines), lines_per_chunk):
        chunk_lines = lines[i:i + lines_per_chunk]
        chunks.append(
            CodeChunk(
                source_path=source.path,
                index=i // lines_per_chunk,
                content="\n".join(chunk_lines)
            )
        )

    return chunks
