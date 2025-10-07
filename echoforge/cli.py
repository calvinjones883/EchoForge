import typer
import yaml
from rich.console import Console
from echoforge.utils import run_github_check, run_etherscan_check

app = typer.Typer(help="EchoForge ⚡ — Web3 & DevOps Automation CLI")
console = Console()


@app.command()
def run(recipe: str = typer.Argument(..., help="Path to YAML automation recipe")):
    """
    Execute a YAML-based automation recipe.
    """
    with open(recipe, "r") as f:
        config = yaml.safe_load(f)

    name = config.get("name", "Unnamed Task")
    console.rule(f"[bold green]🚀 Running recipe: {name}")

    tasks = config.get("tasks", [])
    if not tasks:
        console.print("[yellow]No tasks found in recipe.")
        raise typer.Exit()

    for i, task in enumerate(tasks, start=1):
        t_type = task.get("type")
        console.print(f"\n[cyan]→ Task {i}: {t_type}")
        if t_type == "github_release":
            run_github_check(task)
        elif t_type == "etherscan_verify":
            run_etherscan_check(task)
        else:
            console.print(f"[red]Unknown task type: {t_type}")

    console.rule("[bold green]✅ Done")


if __name__ == "__main__":
    app()
