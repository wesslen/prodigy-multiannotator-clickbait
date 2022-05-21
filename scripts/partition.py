"""Prepare files for ML steps. Converts the JSONL file."""
import typer
import random 
import pathlib
from rich.console import Console
from clumper import Clumper
from pathlib import Path


def partition(input_path: Path, train_jsonl: Path, dev_jsonl: Path):
    random.seed(42)
    console = Console()
    clump = (Clumper.read_jsonl(input_path)
      .mutate(set=lambda d: "dev" if random.random() < 0.5 else "train"))
    
    if pathlib.Path(train_jsonl).exists():
        pathlib.Path(train_jsonl).unlink()
    clump.keep(lambda d: d["set"] == "train").write_jsonl(train_jsonl)
    console.log(f"train jsonl file written at {train_jsonl}")

    if pathlib.Path(dev_jsonl).exists():
        pathlib.Path(dev_jsonl).unlink()
    clump.keep(lambda d: d["set"] == "dev").write_jsonl(dev_jsonl)
    console.log(f"train jsonl file written at {dev_jsonl}")

if __name__ == "__main__":
    typer.run(partition)