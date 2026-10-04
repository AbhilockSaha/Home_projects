from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Crypto Prices")

table.add_column("Coin", style="cyan")
table.add_column("Price", justify="right", style="green")

table.add_row("Bitcoin", "$43,210")
table.add_row("Ethereum", "$3,210")

console.print(table)