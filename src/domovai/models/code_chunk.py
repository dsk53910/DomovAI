from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class CodeChunk:
    source_path: Path
    index: int
    content: str