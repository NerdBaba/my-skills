import sys
import re

# Disco Elysium Colors (ANSI)
COLORS = {
    'INTELLECT': '\033[38;2;77;166;179m',  # Cyan/Blue #4DA6B3
    'PSYCHE': '\033[38;2;98;74;180m',     # Purple #624AB4
    'PHYSIQUE': '\033[38;2;174;60;92m',    # Red/Pink #AE3C5C
    'MOTORICS': '\033[38;2;195;162;43m',   # Yellow #C3A22B
    'WHITE': '\033[38;2;255;255;255m',
    'BOLD': '\033[1m',
    'RESET': '\033[0m'
}

VOICE_TO_CATEGORY = {
    'PHYSICAL INSTRUMENT': 'PHYSIQUE',
    'INLAND EMPIRE': 'PSYCHE',
    'RHETORIC': 'INTELLECT'
}

def render_skill_check(voice, difficulty, result, content):
    category = VOICE_TO_CATEGORY.get(voice.upper(), 'INTELLECT')
    color = COLORS.get(category, COLORS['WHITE'])

    # Format: [VOICE NAME] [Difficulty: Level - Result] — [Content]
    header = f"{COLORS['BOLD']}{color}{voice.upper()}{COLORS['RESET']}"
    meta = f" [{difficulty}: {result}]"

    # Simple line wrapping
    max_width = 80
    prefix = f"{voice.upper()} [{difficulty}: {result}] — "
    indent = " " * len(prefix)

    output = f"\n{header}{meta} — {content}\n"
    print(output)

def parse_and_render(text):
    # Regex to find: **[VOICE NAME]** [Difficulty: Level - Result] — [The Insight]
    pattern = r"\*\*([A-Z ]+)\*\*\s+\[Difficulty:\s+([A-Za-z]+)\s+-\s+([A-Za-z]+)\]\s+—\s+(.*?)(?=\n\*\*|\Z)"
    matches = re.findall(pattern, text, re.DOTALL)

    if not matches:
        # Fallback if the AI didn't use the exact bold format
        pattern_alt = r"([A-Z ]+)\s+\[Difficulty:\s+([A-Za-z]+)\s+-\s+([A-Za-z]+)\]\s+—\s+(.*?)(?=\n[A-Z]|\Z)"
        matches = re.findall(pattern_alt, text, re.DOTALL)

    for voice, diff, res, content in matches:
        render_skill_check(voice.strip(), diff.strip(), res.strip(), content.strip())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            parse_and_render(f.read())
    else:
        parse_and_render(sys.stdin.read())
