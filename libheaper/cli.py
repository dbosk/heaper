"""CLI for heaper - A heap-based to-do list manager."""

import sys
from typing import Optional

import typer

from .heaper import Heaper

app = typer.Typer(help="Heaper - A heap-based to-do list manager")


@app.command("push")
def push(
    priority: int = typer.Argument(..., help="Priority value (lower is higher priority)"),
    content: str = typer.Argument(..., help="The to-do item content"),
    storage: Optional[str] = typer.Option(None, "--storage", "-s", help="Path to storage file"),
):
    """Add an item to the to-do heap."""
    heaper = Heaper(storage_path=storage)
    heaper.push(priority, content)
    typer.echo(f"Added: [{priority}] {content}")


@app.command("pop")
def pop(
    storage: Optional[str] = typer.Option(None, "--storage", "-s", help="Path to storage file"),
):
    """Remove and display the highest priority item."""
    heaper = Heaper(storage_path=storage)
    item = heaper.pop()
    if item is None:
        typer.echo("The to-do list is empty.", err=True)
        raise typer.Exit(1)
    priority, content = item
    typer.echo(f"[{priority}] {content}")


@app.command("peek")
def peek(
    all: bool = typer.Option(False, "--all", "-a", help="Show all items in priority order"),
    storage: Optional[str] = typer.Option(None, "--storage", "-s", help="Path to storage file"),
):
    """View items in the to-do heap."""
    heaper = Heaper(storage_path=storage)
    items = heaper.peek(show_all=all)
    
    if not items:
        typer.echo("The to-do list is empty.")
        return
    
    for priority, content in items:
        typer.echo(f"[{priority}] {content}")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Heaper - A heap-based to-do list manager.
    
    Use pushq, popq, or peekq commands to manage your to-do list.
    """
    if ctx.invoked_subcommand is None:
        # Default behavior: show help if no command provided
        typer.echo(ctx.get_help())


# Create standalone apps for symlinks
pushq_app = typer.Typer(help="Add an item to the to-do heap")
popq_app = typer.Typer(help="Remove and display the highest priority item")
peekq_app = typer.Typer(help="View items in the to-do heap")


@pushq_app.callback(invoke_without_command=True)
def pushq_main(
    ctx: typer.Context,
    priority: int = typer.Argument(..., help="Priority value (lower is higher priority)"),
    content: str = typer.Argument(..., help="The to-do item content"),
    storage: Optional[str] = typer.Option(None, "--storage", "-s", help="Path to storage file"),
):
    """Add an item to the to-do heap."""
    push(priority, content, storage)


@popq_app.callback(invoke_without_command=True)
def popq_main(
    ctx: typer.Context,
    storage: Optional[str] = typer.Option(None, "--storage", "-s", help="Path to storage file"),
):
    """Remove and display the highest priority item."""
    pop(storage)


@peekq_app.callback(invoke_without_command=True)
def peekq_main(
    ctx: typer.Context,
    all: bool = typer.Option(False, "--all", "-a", help="Show all items in priority order"),
    storage: Optional[str] = typer.Option(None, "--storage", "-s", help="Path to storage file"),
):
    """View items in the to-do heap."""
    peek(all, storage)


if __name__ == "__main__":
    app()

