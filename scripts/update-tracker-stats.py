#!/usr/bin/env python3
"""
Script per auto-update statistiche nel tracker.
Usato da GitHub Action.
"""

import re
from pathlib import Path
from datetime import datetime

def count_ideas_by_status(tracker_content):
    """Count ideas for each status"""
    status_counts = {
        '🟢 Done': 0,
        '🟡 In Progress': 0,
        '🔵 To Do': 0,
        '🔵 Documented': 0,
        '🟠 Captured': 0,
        '🔴 On Hold': 0,
        '⚫ Rejected': 0
    }
    
    # Parse table
    for line in tracker_content.split('\n'):
        if line.startswith('|') and not line.startswith('| ID'):
            for status in status_counts.keys():
                if status in line:
                    status_counts[status] += 1
                    break
    
    return status_counts

def update_statistics_section(tracker_content, stats):
    """Update statistics section in tracker"""
    stats_section = f"""## 📈 Statistiche

**Totale Idee:** {sum(stats.values())}
- 🟢 Done: {stats['🟢 Done']}
- 🟡 In Progress: {stats['🟡 In Progress']}
- 🔵 To Do: {stats['🔵 To Do'] + stats['🔵 Documented']}
- 🟠 Captured: {stats['🟠 Captured']}
- 🔴 On Hold: {stats['🔴 On Hold']}
- ⚫ Rejected: {stats['⚫ Rejected']}

**Ultimo Aggiornamento:** {datetime.now().strftime('%Y-%m-%d')}"""
    
    # Replace existing statistics section
    pattern = r'## 📈 Statistiche.*?(?=\n##|\n---|\Z)'
    updated = re.sub(pattern, stats_section, tracker_content, flags=re.DOTALL)
    
    return updated

def main():
    tracker_path = Path('ideas/idea-tracker.md')
    
    if not tracker_path.exists():
        print("⚠️  Tracker file not found")
        return
    
    content = tracker_path.read_text(encoding='utf-8')
    stats = count_ideas_by_status(content)
    updated_content = update_statistics_section(content, stats)
    
    tracker_path.write_text(updated_content, encoding='utf-8')
    print("✅ Tracker statistics updated")

if __name__ == '__main__':
    main()
