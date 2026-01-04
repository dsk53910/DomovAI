from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import typer

from domovai import __version__
from domovai.core.chunker import chunk_source
from domovai.core.loader import load_java_sources

app = typer.Typer(help="Domovai — codebase indexing tool (PoC v0.1)")


def get_version() -> str:
    try:
        return version("domovai")
    except PackageNotFoundError:
        return __version__


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"domovai {get_version()}")
        raise typer.Exit()


@app.callback()
def cli(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show the version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command()
def index(path: Path) -> None:
    sources = load_java_sources(path)
    typer.echo(f"Loaded {len(sources)} Java files")

    total_chunks = 0
    for source in sources:
        chunks = chunk_source(source)
        total_chunks += len(chunks)

    typer.echo(f"Generated {total_chunks} chunks")


@app.command()
def search(query: str) -> None:
    typer.echo(f"Searching: {query}")


@app.command()
def explain(target: str) -> None:
    typer.echo(f"Explaining: {target}")


@app.command()
def stats() -> None:
    typer.echo("Stats: not implemented yet.")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
