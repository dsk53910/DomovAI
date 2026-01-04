import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from domovai.core.chunker import chunk_source
from domovai.core.loader import load_java_sources
from domovai.models.source_file import SourceFile


class TestLoader(unittest.TestCase):
    def test_load_java_sources_reads_only_java_files(self) -> None:
        with TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            java_file = root / "Example.java"
            other_file = root / "README.txt"

            java_file.write_text("class Example {}", encoding="utf-8")
            other_file.write_text("ignore", encoding="utf-8")

            sources = load_java_sources(root)

            self.assertEqual(len(sources), 1)
            self.assertEqual(sources[0].path, java_file)
            self.assertEqual(sources[0].content, "class Example {}")


class TestChunker(unittest.TestCase):
    def test_chunk_source_groups_lines(self) -> None:
        content = "line1\nline2\nline3\nline4\nline5"
        source = SourceFile(path=Path("Example.java"), content=content)

        chunks = chunk_source(source, lines_per_chunk=2)

        self.assertEqual(len(chunks), 3)
        self.assertEqual(chunks[0].index, 0)
        self.assertEqual(chunks[0].content, "line1\nline2")
        self.assertEqual(chunks[1].index, 1)
        self.assertEqual(chunks[1].content, "line3\nline4")
        self.assertEqual(chunks[2].index, 2)
        self.assertEqual(chunks[2].content, "line5")
        self.assertEqual(chunks[0].source_path, source.path)


if __name__ == "__main__":
    unittest.main()
