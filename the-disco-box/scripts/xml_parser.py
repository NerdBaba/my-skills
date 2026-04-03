import re
import sys
import xml.etree.ElementTree as ET


def parse_skill_checks(text):
    # Extract <skill> tags even if they are not at the root
    # Using regex to find blocks because ET.fromstring requires a single root
    matches = re.findall(r"(<skill.*?</skill>)", text, re.DOTALL)

    results = []
    for match in matches:
        try:
            root = ET.fromstring(match)
            results.append(
                {
                    "voice": root.attrib.get("name", "Unknown").upper(),
                    "difficulty": root.attrib.get("difficulty", "Medium"),
                    "success": root.attrib.get("success", "true"),
                    "content": (root.text or "").strip(),
                }
            )
        except Exception as e:
            continue
    return results


if __name__ == "__main__":
    content = sys.stdin.read()
    checks = parse_skill_checks(content)
    for check in checks:
        # Re-format into the standard bold style for the renderer or for display
        print(
            f"**{check['voice']}** [Difficulty: {check['difficulty']} - {'Success' if check['success'].lower() == 'true' else 'Failure'}] — {check['content']}\n"
        )
