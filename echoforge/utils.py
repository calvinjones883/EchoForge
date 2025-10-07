import requests
from rich.console import Console

console = Console()


def run_github_check(task):
    """
    Check latest release of a GitHub repo and print info.
    Example task:
    {
        "type": "github_release",
        "repo": "mina-protocol/mina"
    }
    """
    repo = task.get("repo")
    if not repo:
        console.print("[red]Missing 'repo' field in task.")
        return

    url = f"https://api.github.com/repos/{repo}/releases/latest"
    resp = requests.get(url, timeout=10)

    if resp.status_code == 200:
        data = resp.json()
        console.print(f"[green]Latest release for [bold]{repo}[/bold]: {data['tag_name']}")
    else:
        console.print(f"[red]Failed to fetch release info for {repo}.")


def run_etherscan_check(task):
    """
    Mock example — simulate smart contract verification.
    """
    address = task.get("address", "0x0000...")
    console.print(f"[blue]Verifying contract at {address}...[/blue]")
    # Placeholder for real logic (e.g., etherscan API)
    console.print("[green]Verification successful (mocked).[/green]")
