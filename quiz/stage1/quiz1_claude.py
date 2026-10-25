# 遍历一个文件夹下所有的.txt文件，统计总行数和出现频率最高的10个词

import re
from collections import Counter
from pathlib import Path

FOLDER = Path(r"C:\dev\testTxt")  # 要统计的文件夹
TOP_N = 10
WORD_RE = re.compile(r"[a-z]+(?:'[a-z]+)*")  # 一个词 = 连续的字母，允许 don't、it's 这样的缩写


def tokenize(line: str) -> list[str]:
    """从一行文本里挑出所有单词：统一转小写，弯撇号 ’ 换成直撇号 '。"""
    return WORD_RE.findall(line.lower().replace("’", "'"))


def count_lines_and_words(files: list[Path]) -> tuple[int, Counter[str]]:
    """统计这些文件的总行数和词频。"""
    total_lines = 0
    word_counts = Counter()
    for path in files:
        with path.open(encoding="utf-8") as f:
            for line in f:  # 逐行读，文件再大也只占一行的内存
                total_lines += 1
                word_counts.update(tokenize(line))
    return total_lines, word_counts


def main() -> None:
    if not FOLDER.is_dir():
        raise SystemExit(f"找不到文件夹：{FOLDER}")

    files = sorted(FOLDER.rglob("*.txt"))  # rglob 连子文件夹一起找；只找这一层就用 glob
    total_lines, word_counts = count_lines_and_words(files)

    print(f"Files: {len(files)}")
    print(f"Total lines: {total_lines}")
    print(f"Top {TOP_N} words:")
    for rank, (word, count) in enumerate(word_counts.most_common(TOP_N), start=1):
        print(f"{rank:>2}. {word:<12}{count:>4}")


if __name__ == "__main__":
    main()
