#!/usr/bin/env python3
"""Create a Chinese-named research archive folder structure."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


FOLDERS = [
    ("00_原始资料", "用户提供的 PDF、图片、原始文本抽取、未加工材料。"),
    ("01_资料来源", "文献、网页、产品案例、设计奖项、标准、专利等来源库。"),
    ("02_案例图册", "产品案例图片、案例分析、图片来源说明。"),
    ("03_方向矩阵", "研究方向、产品方向、工作量估算、优先级矩阵。"),
    ("04_方法计划", "调研方法、访谈计划、样本制作、评价量表、时间线。"),
    ("05_计划书改写", "研究目的、研究意义、研究问题、预期成果等可直接替换文本。"),
    ("06_综合报告", "主报告、阶段总结、最终整合报告。"),
    ("07_图片资料", "下载图片、示意图、截图、视觉参考。"),
    ("08_中间文件", "临时抽取文本、草稿、待整理资料。"),
    ("99_归档", "过时版本、旧稿、备份。"),
]


def build_index(project_dir: Path, project_name: str) -> str:
    lines = [
        f"# {project_name}资料夹索引",
        "",
        f"创建日期：{date.today().isoformat()}",
        "",
        "## 项目目的",
        "",
        "本资料夹用于保存研究计划书扩展、文献与案例调研、方向矩阵、方法计划、计划书改写和图片资料。",
        "",
        "## 文件夹结构",
        "",
        "| 文件夹 | 用途 |",
        "|---|---|",
    ]
    for folder, description in FOLDERS:
        lines.append(f"| `{folder}` | {description} |")
    lines.extend(
        [
            "",
            "## 推荐阅读顺序",
            "",
            "1. 先阅读 `06_综合报告` 中的主报告或阶段总结。",
            "2. 再阅读 `01_资料来源` 和 `02_案例图册`，确认资料依据。",
            "3. 用 `03_方向矩阵` 判断研究方向和工作量。",
            "4. 用 `04_方法计划` 安排调研、样本制作和评价。",
            "5. 将 `05_计划书改写` 中的文本整合回研究计划书。",
            "",
            "## 下一步",
            "",
            "请根据当前任务把新文档放入对应分类文件夹，并在本索引中补充重要文件说明。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create Chinese research archive folders.")
    parser.add_argument("project_name", help="中文项目资料夹名称")
    parser.add_argument(
        "--root",
        default=str(Path.home() / "Documents"),
        help="项目资料夹所在根目录，默认 ~/Documents",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser()
    project_dir = root / args.project_name
    project_dir.mkdir(parents=True, exist_ok=True)

    for folder, _ in FOLDERS:
        (project_dir / folder).mkdir(exist_ok=True)

    index_path = project_dir / "00_资料夹索引.md"
    if not index_path.exists():
        index_path.write_text(build_index(project_dir, args.project_name), encoding="utf-8")

    print(project_dir)


if __name__ == "__main__":
    main()
