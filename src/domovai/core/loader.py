from pathlib import Path

from domovai.models.source_file import SourceFile


def load_java_sources(root: Path) -> list[SourceFile]:
    sources: list[SourceFile] = []

    for path in root.rglob("*.java"):
        sources.append(
            SourceFile(
                path=path,
                content=path.read_text(encoding="utf-8"),
            )
        )

    return sources
