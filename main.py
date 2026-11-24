import os

LINE = "I survived three total system crashes, zero documentation, and an unhinged legacy codebase, and today the green tests finally passed on the first run."

def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
