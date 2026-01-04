from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class SourceFile:
    path: Path
    content: str
    language: str = "java"
