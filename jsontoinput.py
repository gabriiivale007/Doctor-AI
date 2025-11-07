from pathlib import Path
import json
from typing import Any, Dict

def converter() -> Dict[str, Any]:
    path = Path(__file__).with_name("input.json")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    data = converter()
    print(data)