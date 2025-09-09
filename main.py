from rich.console import Console
from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T, next: T | None = None) -> None:
        self.data = data

    def __str__(self) -> str:
        return f"{self.data}"


console: Console = Console()

a: Node[int] = Node(1)

console.clear()
console.rule("[bold italic red]Main")
console.print(a)
